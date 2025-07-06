#. Implement Queue using DLL, insert at rear delete from front
class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class QueueDLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = NodeDLL(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        print(f"Dequeued: {temp.data}")

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("None")
print("\nQueue using DLL:")
q2 = QueueDLL()
q2.enqueue(12)
q2.enqueue(200)
q2.enqueue(30)
q2.display()
q2.dequeue()
q2.display()
