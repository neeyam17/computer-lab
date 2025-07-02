class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

if __name__ == "__main__":
    q = Queue()
    q.enqueue("First")
    q.enqueue("Second")
    print("Queue size:", q.size())
    print("Front item:", q.peek())
    print("Dequeued:", q.dequeue())
    print("Queue after dequeue:", q.items)
