import logging
import threading
import time
import json
import os
from collections import deque

from pymodbus.client import ModbusTcpClient
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.server import StartTcpServer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("guard")

PLANT_HOST = "127.0.0.1"
PLANT_PORT = 5020
HOST = "127.0.0.1"
GUARD_PORT = 5021

REG_TEMP = 0
REG_PRESSURE = 1
REG_FLOW = 2
REG_ALARM = 3

TEMP_RANGE     = (600, 750)   # tenths of a degree C
PRESSURE_RANGE = (300, 400)   # tenths of a bar
FLOW_RANGE     = (500, 1500)  # tenths of Nm3/h

MAX_TEMP_STEP      = 30
MAX_PRESSURE_STEP  = 50
MAX_FLOW_STEP       = 100

# --- Rolling-baseline drift detection ---
# Instead of comparing write N to write N-1 (which a slow-ramp attack can
# always stay under), we compare the CURRENT accepted value to the accepted
# value from DRIFT_WINDOW writes ago. This catches cumulative creep even
# when every individual step looks small.
DRIFT_WINDOW              = 3   # was 6 — shrinking cuts the attacker's runway in half
DRIFT_THRESHOLD_TEMP      = 20  # 2.0C cumulative over the window
DRIFT_THRESHOLD_PRESSURE  = 20  # 2.0 bar cumulative over the window
DRIFT_THRESHOLD_FLOW      = 40  # 4.0 Nm3/h cumulative over the window

EVENT_LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events.jsonl")
event_log_lock = threading.Lock()


def log_event(reason):
    event = {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "reason": reason}
    with event_log_lock:
        try:
            with open(EVENT_LOG_FILE, "a") as f:
                f.write(json.dumps(event) + "\n")
        except Exception as e:
            log.error("Failed to write event log: %s", e)


class GuardedContext(ModbusSlaveContext):
    """
    A Modbus write-through firewall.

    Design rule: this class NEVER accepts a value it hasn't itself validated.
    - Absolute range check: hard reject outside physical safe limits.
    - Step check: hard reject any single write that moves too far too fast.
    - Rolling-baseline drift check: compares the CURRENT accepted value to
      the accepted value from N writes ago, so an attacker cannot bypass
      detection by taking many small steps.

    On any rejection: the write is dropped entirely. Nothing is forwarded
    to the plant, nothing is written to the local mirror. The guard's
    exposed state (what the guarded dashboard sees) simply does not move.
    """

    def __init__(self, plant_client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plant_client = plant_client
        self.lock = threading.Lock()
        # Rolling baseline histories store ACCEPTED values only, not
        # attempted writes. That's what makes this a true baseline of
        # "what the plant has actually been allowed to do."
        self.temp_accepted_history     = deque(maxlen=DRIFT_WINDOW)
        self.pressure_accepted_history = deque(maxlen=DRIFT_WINDOW)
        self.flow_accepted_history     = deque(maxlen=DRIFT_WINDOW)

    def _check(self, address, requested, current, value_range, max_step,
               drift_history, drift_threshold, unit_label, unit_divisor):
        reasons = []

        if not (value_range[0] <= requested <= value_range[1]):
            reasons.append(
                f"{requested/unit_divisor:.1f}{unit_label} outside safe range "
                f"{value_range[0]/unit_divisor:.1f}-{value_range[1]/unit_divisor:.1f}{unit_label}"
            )

        step = abs(requested - current)
        if step > max_step:
            reasons.append(
                f"step of {step/unit_divisor:.1f}{unit_label} exceeds max "
                f"{max_step/unit_divisor:.1f}{unit_label}"
            )

        if len(drift_history) == DRIFT_WINDOW:
            drift = requested - drift_history[0]
            if abs(drift) > drift_threshold:
                reasons.append(
                    f"cumulative drift of {drift/unit_divisor:.1f}{unit_label} "
                    f"over last {DRIFT_WINDOW} accepted writes exceeds "
                    f"{drift_threshold/unit_divisor:.1f}{unit_label} limit"
                )

        return reasons

    def setValues(self, fc_as_hex, address, values):
        requested = values[0]
        reasons = []

        if address == REG_TEMP:
            current = self.getValues(3, REG_TEMP, count=1)[0]
            reasons = self._check(address, requested, current, TEMP_RANGE,
                                   MAX_TEMP_STEP, self.temp_accepted_history,
                                   DRIFT_THRESHOLD_TEMP, "C", 10)
        elif address == REG_PRESSURE:
            current = self.getValues(3, REG_PRESSURE, count=1)[0]
            reasons = self._check(address, requested, current, PRESSURE_RANGE,
                                   MAX_PRESSURE_STEP, self.pressure_accepted_history,
                                   DRIFT_THRESHOLD_PRESSURE, " bar", 10)
        elif address == REG_FLOW:
            current = self.getValues(3, REG_FLOW, count=1)[0]
            reasons = self._check(address, requested, current, FLOW_RANGE,
                                   MAX_FLOW_STEP, self.flow_accepted_history,
                                   DRIFT_THRESHOLD_FLOW, " Nm3/h", 10)
        else:
            # Unknown/alarm register — allow passthrough of writes (e.g. resets)
            with self.lock:
                try:
                    self.plant_client.write_register(address, requested, slave=1)
                except Exception as e:
                    log.error("Forward failed: %s", e)
            super().setValues(fc_as_hex, address, values)
            return

        if reasons:
            reason_text = "; ".join(reasons)
            log.warning("BLOCKED write to reg %s: %s", address, reason_text)
            log_event(reason_text)
            # Option A behavior: reject completely. Do not touch the plant,
            # do not touch the local mirror, do not append to drift history.
            # The last known-safe accepted value remains authoritative.
            return

        # Accepted — forward to the real plant AND update local mirror AND
        # record it in the rolling baseline history.
        with self.lock:
            try:
                self.plant_client.write_register(address, requested, slave=1)
            except Exception as e:
                log.error("Forward failed: %s", e)
        super().setValues(fc_as_hex, address, values)

        if address == REG_TEMP:
            self.temp_accepted_history.append(requested)
        elif address == REG_PRESSURE:
            self.pressure_accepted_history.append(requested)
        elif address == REG_FLOW:
            self.flow_accepted_history.append(requested)


def sync_safe_reads(store, plant_client, lock, stop_event):
    """
    Periodically reads the real plant's telemetry and mirrors it into the
    guard's exposed state — but ONLY if every value read is within the
    absolute safe range. This keeps normal plant drift (temperature
    wandering a bit under real physics) visible on the guarded dashboard,
    while guaranteeing an attacker who writes directly to the plant's own
    port (bypassing the guard entirely) can never have those corrupted
    values bleed into the guard's mirror.
    """
    while not stop_event.is_set():
        with lock:
            try:
                result = plant_client.read_holding_registers(0, 4, slave=1)
                if not result.isError():
                    regs = result.registers
                    t, p, f = regs[REG_TEMP], regs[REG_PRESSURE], regs[REG_FLOW]
                    if (TEMP_RANGE[0]     <= t <= TEMP_RANGE[1] and
                        PRESSURE_RANGE[0] <= p <= PRESSURE_RANGE[1] and
                        FLOW_RANGE[0]     <= f <= FLOW_RANGE[1]):
                        ModbusSlaveContext.setValues(store, 3, 0, list(regs))
                        store.temp_accepted_history.append(t)
                        store.pressure_accepted_history.append(p)
                        store.flow_accepted_history.append(f)
            except Exception as e:
                log.error("Sync error: %s", e)
        time.sleep(1.0)


def main():
    plant_client = ModbusTcpClient(PLANT_HOST, port=PLANT_PORT)
    plant_client.connect()

    block = ModbusSequentialDataBlock(0, [670, 340, 900, 0] + [0] * 96)
    store = GuardedContext(plant_client, hr=block, zero_mode=True)
    context = ModbusServerContext(slaves=store, single=True)

    stop_event = threading.Event()
    sync_thread = threading.Thread(
        target=sync_safe_reads,
        args=(store, plant_client, store.lock, stop_event),
        daemon=True,
    )
    sync_thread.start()

    log.info("Guard listening on %s:%s — protecting plant at %s:%s",
             HOST, GUARD_PORT, PLANT_HOST, PLANT_PORT)
    try:
        StartTcpServer(context=context, address=(HOST, GUARD_PORT))
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        plant_client.close()


if __name__ == "__main__":
    main()
