import tracemalloc
import time
import os 
import psutil

def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
# start memory tracking 
tracemalloc.start()

arr = list(range(1000, 0 , -1))
bubble_sort(arr)

# stop memory tracking 
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
# cpu and time 
process = psutil.Process(os.getpid())
cpu_usage = process.cpu_percent(interval=1)

print(f"===Memory Usage===")
print(f"Current memory: {current / 1024 / 1024:.2f} KB")
print(f"Peak memory: {peak / 1024 / 1024:.2f} KB")

print("\n=== CPU Usage ===")
print(f"User CPU time: {psutil.cpu_times().user:.4f} seconds")
print(f"System CPU time: {psutil.cpu_times().system:.4f} seconds")

print("\n=== Array Check ===")
print(f"First 5 elements: {arr[:5]}")
print(f"Last 5 elements: {arr[-5:]}")