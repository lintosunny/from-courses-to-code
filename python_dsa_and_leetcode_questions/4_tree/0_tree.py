# A Tree is a hierarchical, non-linear data structure made up of nodes connected by edges, with a single root node.
# Node: Basic element of a tree
# Root: Topmost node
# Parent Node: A node that has one or more children
# Child Node: A node derived from another node
# Leaf Node: Node with no children
# Subtree: Tree formed by a node and its descendants
# Depth: Distance from root to a node
# Height: Longest path from root to a leaf
# Time complexity: O(n) (skewed tree)

# Full Binary Tree: Every node has 0 or 2 children. No node has exactly 1 child.
# Perfect Binary Tree: All nodes have 2 children (except leaves). All leaf nodes are at the same level. Total nodes = 2^h - 1
# Complete Binary Tree: All levels are filled except possibly the last. Last level is filled from left to right.

# Binary Search Tree
# Values smaller than the root are stored on the left and larger values are stored on the right.

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

    def contains(self, value):
        if self.root is None:
            return False 
        temp = self.root 
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False



my_tree = BinarySearchTree()
print(my_tree.root)
my_tree.insert(10)
print(my_tree.root.value)
my_tree.insert(200)
print(my_tree.root.right.value)
my_tree.insert(50)
print(my_tree.root.right.left.value)
print(my_tree.contains(200))