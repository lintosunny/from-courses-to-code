# Linked list don't have index
# contigous space in a memory, unlike list that is continuos space 
# Head, points to first node in the linked list
# Tail, points to last node
# Each node is points to next and last one to None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        


my_linked_list = LinkedList(4)
my_linked_list.append(8)
print(my_linked_list.print_list())