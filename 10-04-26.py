import threading
import time
import psutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def memory_check():
    while True:
        ram = psutil.virtual_memory()
        logging.info(f"Memory Usage: {ram.percent}%")
        time.sleep(2)

def status_update():
    while True:
        cpu = psutil.cpu_percent()
        logging.info(f"System status: CPU at {cpu}%")
        time.sleep(3)

def save_report():
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        with open("report.txt", "a") as f:
            f.write(f"CPU: {cpu}% | RAM: {ram}%\n")
        logging.info("Report saved!")
        time.sleep(5)
            
            # create threads
t1 = threading.Thread(target=memory_check, daemon=True)
t2 = threading.Thread(target=status_update, daemon=True)
t3 = threading.Thread(target=save_report, daemon=True)

# start all threads
t1.start()
t2.start()
t3.start()

# let it run for 10 seconds
logging.info("Scheduler started! Running for 10 seconds...")
time.sleep(10)
logging.info("Scheduler stopped!")
            
       
    