import os
import platform
import psutil
import logging
import json
import time
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("system_info.log"),
        logging.StreamHandler()
    ]
)
def get_memory_info():
    mem = psutil.virtual_memory()
    return{
        "total": round(mem.total / (1024 ** 3), 2),
        "available": round(mem.available / (1024 ** 3), 2),
        "percent": mem.percent
    }
def save_info(data, filename="system_info.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
def get_system_info():
    return{
        "os": platform.system(),
        "version": platform.version(),
        "processor": platform.processor(),
        
    }
if __name__ == "__main__":
    start = time.perf_counter()
    logging.info("Dashboard starting...")
    sys_info = get_system_info()
    mem_info = get_memory_info()
    report = {
        "system": sys_info,
        "memory": mem_info
    }
    save_info(report)
    logging.info("Report saved to system_info.json")
    end = time.perf_counter()
    logging.info(f"Dashboard finished in {end - start:.6f} seconds")
