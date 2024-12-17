class EmptyQueueError(Exception):
    pass

class Queue:
    
    def __init__(self):
        self.items = []
        self.front = 0
    
    def is_empty(self):
        return self.front == len(self.items)

    def size(self):
        return len(self.items) - self.front 
    
    def enqueue(self, item):
        return self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return EmptyQueueError("Queue is Empty and no insertions are supported")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = self.front + 1
        return x

    def display(self):
        print(self.items)
    
    def peek(self):
        """
        Return first element in the Queue
        """
        if self.is_empty():
            return EmptyQueueError("Queue is Empty")
        return self.items[self.front]
    
if __name__ == "__main__":
    qe = Queue()

    while True:
        choice = int(input(" Enter your choice"))

        if choice == 1:
            x = int(input("Enter the element"))
            qe.enqueue(x)
        elif choice == 2:
            x = qe.dequeue()
            print("deleted the element: ",x)
        elif choice == 3:
            print("Size of the queue", qe.size())
        elif choice == 4:
            qe.display()
        else:
            print("Wrong choice. Please select from the available choices")

