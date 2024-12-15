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
        p = sel.start
        n = 0
        while p is not None:
            n+=1
            p = p.link
        print("count of nodes in list is = ", n)

    def search(self, x)
        position = 1
        p = selft.start
        while p is not None:
            if p.info == x:
                print(x, "is found at ", position)
                return True
            position += 1
            p = p.link
        else:
            print(" Element is not found")
            return false







            

