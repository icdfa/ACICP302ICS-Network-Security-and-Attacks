from pymodbus.client import ModbusTcpClient
import threading
import time
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5020

print(f"--- DOS FLOOD: port {PORT} ---")
def flood(tid):
    client = ModbusTcpClient(HOST, port=PORT)
    try: client.connect()
    except: pass
    for _ in range(20):
        try: client.read_holding_registers(0, 4, slave=1)
        except: pass
        time.sleep(0.05)
    client.close()

threads = [threading.Thread(target=flood, args=(i,)) for i in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print("Done. 200 requests sent.")
