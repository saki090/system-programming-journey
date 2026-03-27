import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# --- Testing the Stack ---
s = Stack()

print("=== Pushing items ===")
s.push(10)
s.push(20)
s.push(30)
print(f"Pushed 10, 20, 30")
print(f"Stack size: {s.size()}")
print(f"Top item (peek): {s.peek()}")

print("\n=== Popping items ===")
print(f"Popped: {s.pop()}")
print(f"Popped: {s.pop()}")
print(f"Stack size now: {s.size()}")

print("\n=== Edge case ===")
s.pop()
print(f"Popping from empty stack: {s.pop()}")
