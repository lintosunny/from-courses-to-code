class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node 
            return True

        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False 

            if temp.value < new_node.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False 
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

my_tree = BinarySearchTree()
my_tree.r_insert(23)
my_tree.r_insert(3)
my_tree.r_insert(31)

print(f"root: {my_tree.root.value}")
print(f"Root -> Left: {my_tree.root.left.value}")
print(f"Root -> Right: {my_tree.root.right.value}")

print(f"BST contains 31: {my_tree.r_contains(31)}")
print(f"BST contains 2: {my_tree.r_contains(2)}")