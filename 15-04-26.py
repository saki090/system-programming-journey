import psutil
import json
import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu_percent": proc.info['cpu_percent'],
                "memory_percent": proc.info['memory_percent']
            })
        except:
            pass
    return processes
def save_processes(data, filename="processes.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
if __name__ == "__main__":
    start = time.perf_counter()
    logging.info("Process dashboard starting...")
    processes = get_processes()
    save_processes(processes)
    logging.info("Process report saved to processes.json")
    end = time.perf_counter()
    logging.info(f"Process dashboard finished in {end - start:.6f} seconds")
    
