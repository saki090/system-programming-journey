import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22]
print(f"Original list: {arr}")

start = time.perf_counter()
bubble_sort(arr)
end = time.perf_counter()

print(f"Sorted list: {arr}")
print(f"\nTime taken: {(end - start):.6f} seconds")