class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

# Stack - Last In First Out
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node 
        self.height = 1 

    def print_stack(self):
        temp = self.top 
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node 
        self.height += 1 

    def pop(self):
        if self.height == 0:
            return None 
        else:
            temp = self.top 
            self.top = self.top.next 
            temp.next = None 
        self.height -= 1 
        return temp


my_stack = Stack(4)
my_stack.print_stack()
print("-"*10)
my_stack.push(5)
my_stack.print_stack()
print("-"*10)
my_stack.pop()
my_stack.print_stack()
print("-"*10)


# Queue - First In First Out
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node
        self.length = 1 

    def print_queue(self):
        temp = self.first 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    # add value to last(tail). so, O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node 
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1 
        return True
    
    # remove value from first(head). so, O(1)
    # remove value to the last has O(n)
    def dequeue(self):
        if self.first is None:
            return None
         
        temp = self.first 
        if self.length == 1:
            self.first = None 
            self.last = None
        else:
            self.first = self.first.next 
            temp.next = None 
        self.length -= 1 
        return temp


        

            

my_queue = Queue(14)
my_queue.print_queue()
print("-"*10)
my_queue.enqueue(15)
my_queue.print_queue()
print("-"*10)
my_queue.dequeue()
my_queue.print_queue()
print("-"*10)