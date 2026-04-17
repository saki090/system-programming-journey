import socket
import json
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def scan_host(host, ports):
    open_ports = []
    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)
            logging.info(f"Port {port} is OPEN!")
    return open_ports  # ← outside the loop!

def save_results(results, filename="scan_results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    target = "localhost"
    ports_to_scan = [14217, 24006, 29306, 32470, 39254, 51090, 56573]
    start = time.perf_counter()
    logging.info(f"Scanning {target}...")
    open_ports = scan_host(target, ports_to_scan)
    save_results({"host": target, "open_ports": open_ports})
    logging.info(f"Open ports: {open_ports}")
    logging.info(f"Scan done in {time.perf_counter() - start:.6f} seconds")
                    