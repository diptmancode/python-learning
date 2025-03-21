# Implementing Singly Linked List


class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

  

class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None
    
    def print_list(self):
        if self.is_empty():
            print("List is empty")
        else:
            print("----------")
            temp = self.start
            while temp is not None:
                print(temp.item, " ")
                temp = temp.next

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        # if list is empty
        if self.start is None:
            self.start = new_node
            return
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def search(self, data):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
        
    

sll = SLL()
sll.insert_at_start(20)
sll.insert_at_start(10)
sll.insert_at_end(30)
sll.print_list()
print(sll.search(20))
