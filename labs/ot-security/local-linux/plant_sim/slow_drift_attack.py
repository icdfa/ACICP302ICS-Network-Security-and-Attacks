from pymodbus.client import ModbusTcpClient
import time
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

client = ModbusTcpClient(HOST, port=PORT)
client.connect()
before = client.read_holding_registers(0, 4, slave=1)
current = before.registers[1]
print(f"Starting: {current/10:.1f} bar | Target: port {PORT}")
for i in range(12):
    current += 10
    client.write_register(1, current, slave=1)
    time.sleep(2)
    actual = client.read_holding_registers(0, 4, slave=1).registers[1]
    print(f"  Step {i+1}: requested {current/10:.1f} -> actual {actual/10:.1f}")
client.close()
