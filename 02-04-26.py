import os 
import platform
import psutil
import time
start = time.perf_counter()
print("===System Info===")
print(f"OS: {platform.system()}")
print(f"OS Version: {platform.version()}")
print(f"Processor: {platform.processor()}")

print("\n===CPU & RAM===")
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

ram = psutil.virtual_memory()
print(f"Total RAM: {round(ram.total/(1024**3), 2)}GB")
print(f"Available RAM: {round(ram.available/(1024**3), 2)}GB")
print(f"RAM Used: {ram.percent}%")

print("\n===Directory Info===")
print(f"Current Directory: {os.getcwd()}")
print(f"Files here: {os.listdir('.')}")

end = time.perf_counter()
print(f"\nTime taken: {(end - start):.6f} seconds")
