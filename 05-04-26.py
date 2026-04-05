import threading
import time 
def count_up():
    for i in range(5):
        print(f"Count: {i}")
        time.sleep(0.5)
        
def f1_driver():
    drivers = ["Antonelli", "Russell", "Norris", "Sainz", "Perez"]
    for driver in drivers:
        print(f"Driver: {driver}")
        time.sleep(0.5)

start = time.perf_counter()
t1 = threading.Thread(target=count_up)
t2 = threading.Thread(target=f1_driver)
t1.start()
t2.start()
t1.join()
t2.join()
end = time.perf_counter()
print(f"Execution time: {end - start:.2f} seconds")