import time 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
       self.head = None
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        while current is not None:
            print(current.value,end="→")
            current = current.next
        print("None")

# ---- Now i am going test it with a timer-----
start = time.perf_counter()

ll = Linkedlist()

print("=== Edge case - empty list ===")
ll.display()

print("=== Appending items ===")
ll.append(10)
ll.append(20)
ll.append(30)
print("Appended: 10, 20, 30")

print("=== Display ===")
ll.display()

end = time.perf_counter()
print(f"\nTime taken: {(end - start):.6f} seconds")



       

    
     
