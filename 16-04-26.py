import psutil
import time

class ProcessData:
    # __slots__ tells Python not to create a dictionary for every instance
    # This is a "pro" move for systems programming in Python
    __slots__ = ['pid', 'name', 'cpu', 'mem']
    
    def __init__(self, pid, name, cpu, mem):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.mem = mem

def stream_processes():
    """A generator that yields process data one by one."""
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            p_info = proc.info
            yield ProcessData(
                p_info['pid'], 
                p_info['name'], 
                p_info['cpu_percent'], 
                p_info['memory_percent']
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    print(f"{'PID':<10} | {'NAME':<25} | {'CPU%':<10}")
    print("-" * 50)
    
    # Streaming data instead of loading everything into a giant list
    for p in stream_processes():
        if p.cpu > 1.0:  # Only show active processes
            print(f"{p.pid:<10} | {p.name[:25]:<25} | {p.cpu:<10}")