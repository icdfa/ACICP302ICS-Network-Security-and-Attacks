import logging
import random
import threading
import time

from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.server import StartTcpServer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("plant")

REG_TEMP = 0
REG_PRESSURE = 1
REG_FLOW = 2
REG_ALARM = 3

TEMP_RANGE = (600, 750)
PRESSURE_RANGE = (300, 400)
FLOW_RANGE = (500, 1500)

UPDATE_INTERVAL_SEC = 1.0
HOST = "0.0.0.0"
PORT = 5020


def clamp(value, low, high):
    return max(low, min(high, value))


class ReactiveDataBlock(ModbusSequentialDataBlock):
    """A data block that tracks when values are externally written,
    and uses those as the new base for drift — instead of silently
    overwriting them with the simulator's internal state."""

    def __init__(self, address, values):
        super().__init__(address, values)
        self._internal = {
            REG_TEMP: 670,
            REG_PRESSURE: 340,
            REG_FLOW: 900,
        }
        self._lock = threading.Lock()

    def setValues(self, address, values):
        with self._lock:
            for i, val in enumerate(values):
                reg = address + i
                if reg in self._internal:
                    self._internal[reg] = val
        super().setValues(address, values)

    def get_internal(self, reg):
        with self._lock:
            return self._internal.get(reg, 0)

    def set_internal(self, reg, val):
        with self._lock:
            self._internal[reg] = val


def simulate_normal_operation(store, block, stop_event):
    while not stop_event.is_set():
        temp = clamp(block.get_internal(REG_TEMP) + random.randint(-2, 2), *TEMP_RANGE)
        pressure = clamp(block.get_internal(REG_PRESSURE) + random.randint(-3, 3), *PRESSURE_RANGE)
        flow = clamp(block.get_internal(REG_FLOW) + random.randint(-10, 10), *FLOW_RANGE)

        block.set_internal(REG_TEMP, temp)
        block.set_internal(REG_PRESSURE, pressure)
        block.set_internal(REG_FLOW, flow)

        store.setValues(3, REG_TEMP, [temp])
        store.setValues(3, REG_PRESSURE, [pressure])
        store.setValues(3, REG_FLOW, [flow])

        alarm = 1 if pressure >= PRESSURE_RANGE[1] - 5 else 0
        store.setValues(3, REG_ALARM, [alarm])

        log.info(
            "telemetry temp=%.1fC pressure=%.1fbar flow=%.1fNm3/h alarm=%s",
            temp / 10, pressure / 10, flow / 10, alarm,
        )
        time.sleep(UPDATE_INTERVAL_SEC)


def main():
    initial_values = [670, 340, 900, 0]
    block = ReactiveDataBlock(0, initial_values + [0] * 96)
    store = ModbusSlaveContext(hr=block, zero_mode=True)
    context = ModbusServerContext(slaves=store, single=True)

    stop_event = threading.Event()
    sim_thread = threading.Thread(
        target=simulate_normal_operation,
        args=(store, block, stop_event),
        daemon=True,
    )
    sim_thread.start()

    log.info("Plant simulator listening on %s:%s (no protection layer active)", HOST, PORT)
    try:
        StartTcpServer(context=context, address=(HOST, PORT))
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()


if __name__ == "__main__":
    main()
