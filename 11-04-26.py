import timeit
import random
import time

# creating a random list of numbers
random_list = [random.randint(1, 100) for _ in range(1000)]
def bubble_sort(arr):
    arr = arr.copy()  # don't modify original!
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def manual_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False
# now i will creating a benchmarking function to test the performance of sorting the list
def benchmark_sorting():
    sorted_list = bubble_sort(random_list)
    return sorted_list
def benchmark_searching():
    target = random.choice(random_list)
    found = manual_search(random_list, target)
    return found
# now i will run the benchmarks and print the results
if __name__ == "__main__":
    # sorting comparison
    bubble_time = timeit.timeit(lambda: bubble_sort(random_list), number=100)
    builtin_time = timeit.timeit(lambda: sorted(random_list), number=100)

    # searching comparison
    target = random.choice(random_list)
    manual_time = timeit.timeit(lambda: manual_search(random_list, target), number=1000)
    in_time = timeit.timeit(lambda: target in random_list, number=1000)

    # print results
    print("\n=== Sorting Benchmark ===")
    print(f"{'Bubble Sort':<20} {bubble_time:.6f}s")
    print(f"{'Built-in sorted()':<20} {builtin_time:.6f}s")
    print(f"Winner: {'Built-in sorted()' if builtin_time < bubble_time else 'Bubble Sort'} 🏆")

    print("\n=== Search Benchmark ===")
    print(f"{'Manual search':<20} {manual_time:.6f}s")
    print(f"{'in operator':<20} {in_time:.6f}s")
    print(f"Winner: {'in operator' if in_time < manual_time else 'Manual search'} 🏆")