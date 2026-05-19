# --------------------------------
# WHAT IS A HASH TABLE?
# --------------------------------
# A Hash Table is a data structure used to store data in key-value pairs.
#
# Example:
# {
#     "name": "Linto",
#     "age": 25
# }
#
# It provides very fast:
# - insertion
# - searching
# - deletion
#
# Average Time Complexity:
# O(1)


# --------------------------------
# HOW HASH TABLE WORKS
# --------------------------------
# A hash function converts a key into an index number.
#
# Example:
# key = "apple"
#
# hash_function("apple") -> 3
#
# Data gets stored at index 3
# inside an array.


# --------------------------------
# COLLISION
# --------------------------------
# Collision happens when two keys get the same index.
#
# Example:
# "apple"  -> index 3
# "grapes" -> index 3
#
# Both trying to store data in same location.


# --------------------------------
# SEPARATE CHAINING
# --------------------------------
# In Separate Chaining, each array index stores multiple values using a Linked List.
#
# Example:
#
# index 3:
# ["apple"] -> ["grapes"] -> ["mango"]
#
# If collision happens, new data is added to the linked list.


# --------------------------------
# LINEAR PROBING
# --------------------------------
# In Linear Probing, if an index is full, move to the next empty index.
#
# Example:
#
# index 3 -> occupied
# check index 4
# check index 5
#
# First empty spot is used.


# --------------------------------
# LINKED LIST
# --------------------------------
# A Linked List is a chain of nodes.
#
# Each node contains:
# - data
# - pointer to next node
#
# Example:
#
# [10] -> [20] -> [30] -> None
#
# Used in Separate Chaining to handle collisions.

# ---------------------------------
# Big O
# ---------------------------------
# set item (Insert) O(1)
# get item (Lookup) O(1) - collision is rare in advanced has and large name space, one like in dictionary implemented in python


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size 

    def __hash(self, key):
        my_hash = 0 
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash 
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print(my_hash_table.get_item('bolts'))
print(my_hash_table.keys())