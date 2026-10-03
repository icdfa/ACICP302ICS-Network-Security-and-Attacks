from pymodbus.client import ModbusTcpClient
import time
import sys

HOST = "192.168.2.139"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

print(f"--- RECON SCAN: port {PORT} ---")
client = ModbusTcpClient(HOST, port=PORT)
client.connect()
for start in range(0, 50, 10):
    result = client.read_holding_registers(start, 10, slave=1)
    if not result.isError():
        print(f"  Regs {start}-{start+9}: {result.registers}")
    time.sleep(0.1)
client.close()
