class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self, max_items=10):
        self.items = [None] * max_items
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
    def push(self, x):
        if self.is_full():
            return "stack is full and cannot insert values"
        self.items[self.count] = x
        self.count += 1

    def is_full(self):
        return self.count == len(self.items)
    
    def pop(self, item):
        if self.is_empty():
            return "Stack is empty"
        x = self.items[self.count - 1]
        self.items[self.count -1 ] = None 
        self.count -= 1
        return x
    
    def peek(self):
        if self.items.empty():
            print("No elements in the stack")
            return
        return self.items[-1]
    
    def display(self):
        print(self.items)

if __name__ == "__main__":
    st = Stack()

    while True:
        choice = int(input("Enter your choice:   "))
        if choice == 1:
            x = int(input(" Enter the element to be pushed: "))
            st.push(x)
        elif choice == 2:
            x = int(input(" Enter the element to be remove: "))
            st.pop(x)
        elif choice == 3:
            print("size of the stack is : ",st.size())
        elif choice == 4:
            st.display()
        else:
            print("wrong choice")
