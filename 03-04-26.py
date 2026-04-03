import os
import time

start = time.perf_counter()

print("=== Process Info ===")
print(f"My PID: {os.getpid()}")
print(f"Parent PID: {os.getppid()}")
print(f"Current User: {os.environ.get('USER', 'unknown')}")

print("\n=== Running a shell command ===")
os.system("echo Hello from the OS!")

print("\n=== Environment Variables ===")
print(f"Home: {os.environ.get('HOME')}")
print(f"Path: {os.environ.get('PATH')}")

end = time.perf_counter()
print(f"\nTime taken: {(end - start):.6f} seconds")