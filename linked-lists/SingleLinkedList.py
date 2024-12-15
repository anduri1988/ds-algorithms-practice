class Node:
    
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    
    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            p = self.start
            print("displaying lists")
            while p is not None:
                print(p.info)
                p = p.link # Next node
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n+=1
            p = p.link
        print("count of nodes in list is = ", n)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is found at ", position)
                return True
            position += 1
            p = p.link
        else:
            print(" Element is not found")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    
    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp
    
    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)
    
    def insert_after(self, data, x):
        pass
    
    def insert_before(self, data, x):
        pass
    
    def insert_at_positio(self, x):
        pass
    
    def delete_node(self, x):
        pass
    
    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass
     
    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass
    
    def buddle_sort_exlinks(self):
        pass
    
    def has_cycle(self):
        pass

    def find_cycle(self):
        pass
    
    def remove_cycle(self):
        pass
    
    def insert_cycle(self):
        pass
    
    def merge2(self, list2):
        pass
    
    def _merge2(self, p1, p2):
        pass
    
    def merge_sort(self):
        pass
    
    def merge_sort_rec(self, liststart):
        pass
    
    def divide_list(self):
        pass
    
###################################################################################

list = SingleLinkedList()
list.create_list()

while True:
   option = int(input("Enter your choice: " ) )
   if option == 1:
     list.display_list()
   elif option == 2:
        list.count_nodes()
   elif option == 3:
        data = int(input('Enter element to be searched: '))
        list.search(data)
   elif option == 4:
    data = int(input('Enter element to be inserted: '))
    list.insert_in_beginning(data)
   elif option == 5:
    data = int(input('Enter element to be inserted: '))
    list.insert_at_end(data)
   elif option == 6:
    data = int(input('Enter element to be inserted: '))
    x = int(input('Enter element after which to insert: '))
    list.insert_after(data, x)









            

