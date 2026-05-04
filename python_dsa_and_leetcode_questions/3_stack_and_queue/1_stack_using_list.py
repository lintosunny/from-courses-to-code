# Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.
class Stack:
    def __init__(self):
        self.stack_list = []

# Custom methods 
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

# Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.
    def push(self, value):
        self.stack_list.append(value)

# Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.
    def pop(self):
        if self.is_empty():
            return None 
        else:
            return self.stack_list.pop()