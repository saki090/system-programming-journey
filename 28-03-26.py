import time

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # add to back

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items.pop(0)  # remove from front

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.items[0]  # front item

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---- Time taken and testing the queue ----
start = time.perf_counter()
q = Queue()
print("===Enqueuing items===")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(f"Enqueued: 10, 20, 30")
print(f"Queue size: {q.size()}")
print(f"Front item(peek): {q.peek()}")
print("===Dequeuing items===")
print(f"Dequeued: {q.dequeue()}")
print(f"Dequeued: {q.dequeue()}")
print(f"Queue size right now: {q.size()}")
print("\n===Edge case===")
q.dequeue()
print(f"Dequeuing from empty queue: {q.dequeue()}")
end = time.perf_counter()
print(f"Time taken: {end - start} seconds")
