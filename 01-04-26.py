import time 
import sys
start = time.perf_counter()
# integers
a = 10
b = 999999999
# strings
s1 = "hi"
s2 = "hello world"
# lists
l1 = []
l2 = [1, 2, 3, 4, 5]
print("===Integers===")
print(f"a = {a} → size: {sys.getsizeof(a)} bytes, id: {id(a)}")
print(f"b = {b} → size: {sys.getsizeof(b)} bytes, id: {id(b)}")

print("===Strings===")
print(f"s1 = {s1} → size: {sys.getsizeof(s1)} bytes id: {id(s1)}")
print(f"s2 = {s2} → size: {sys.getsizeof(s2)} bytes id: {id(s2)}")

print("===Lists===")
print(f"l1 = {l1} → size: {sys.getsizeof(l1)} bytes, id: {id(l1)}")
print(f"l2 = {l2} → size: {sys.getsizeof(l2)} bytes, id: {id(l2)}")

end = time.perf_counter()
print(f"\nTime taken: {(end - start):.6f} seconds")
