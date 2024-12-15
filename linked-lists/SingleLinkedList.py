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
        pass
    
    def insert_at_end(self, data):
        pass
    
    def create_list(self):
        pass
    
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
   option = int(input("Enter your choice:" ) )
   if option == 1:
     list.display_list()
   elif option == 2:
        list.count_nodes()
   elif option == 3:
        data = int(input('Enter element to be searched'))
        list.search(data)








            

