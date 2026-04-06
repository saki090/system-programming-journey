import logging
import time 
# set up logging 
logging.basicConfig(
    level = logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("system_log.txt"),
        logging.StreamHandler() 
    ]
)
start = time.perf_counter()
logger = logging.getLogger(__name__)
logger.debug("Checking the system variables...")
logger.info("System started successfully.")
logger.warning("CPU usage is getting high.")
logger.error("Failed to read configuration file.")
logger.critical("System is out of memory!")

end = time.perf_counter()
logger.info(f"Program executed in {end - start:.6f} seconds.")