# Lists
# Lists are mutable so it don't create a soft copy by default. but if we use concate or slice we can create a soft copy and changes in original won't reflect here
# extend a list, we can use + but it can create a new list. but we have to extend the existing list
# list1.append(v): extend list1 by a single value v
# list1.extend(list2): extend list1 by a list of values
# list1.remove(x): removes first occurence of x, error if no occurence of x in list1
# we can also modify slice, list1[2:] = [7,8]
# can expand or shrink slice instead of 2 if we pass 3 values it will expand and vice verca
# List membership: x in l, returns True if value x is found in list l
# l.reverse(), l.sort(), l.index(x): find the left most index of x, l.rindex(x): find the right most index of x
# don't forget to assign a value to a name before it is first used. x = 0, l = []

# Breaking out a Loop
# for i in l: repeat body for each item in list l
# while condition: repeat body till condition become false
# can exit prematurely from loop using `break`
# continue, skip the current one and go to next one

# Array vs List
# Array
# single block of memory, elements of uniform type, typically size of sequence fixed in advance
# indexing is fast, accessing seq[i] is fast
# but insertion and contraction are expensive
# Lists
# python lists are lists not arrays
# values scattered in memory, each element point to next `linked list`, flexible size
# follow i links to access seq[i], cost propotional to i
# plumbing - inserting or deleting an element is easy
# exchange seq[i] and seq[j] - constant time in array, linear time in lists
# delete seq[i] or insert v after seq[i] - constant time in lists, linear time in array
# algorithms on one data structure may not transfer to another, like binary search
# binary search only work in arrays and time is O(log n). by seeing only a fraction of the sequence we can conclude that element is presnt or not

def binarySearch(seq, v, l, r):
    if (r - l) == 0:
        return False 
    
    mid = (l + r) // 2

    if v == seq[mid]:
        return True
    
    if v < seq[mid]:
        return binarySearch(seq, v, l, mid)
    else:
        return binarySearch(seq, v, mid+1 , r)
    
# Efficiency
# measures time taken by an algorithm as a function T(n) with respect to input size n
# usually report in worst case behaviour - worst case for searching in a sequence is when value is not found
# O() notation - Interested in broad relationship between input size and running time, O(log n), O(n), , O(n log n), O(n^2), O(2^n)...

# Sorting
# Searching becomes more efficient if we have a sorted array
# searching in unsorted array, linear scan, O(n)
# searching in sorted array, binary search, O(log n)

# selection sort
# select the next element in a sorted order
# move it in to correct place in the final sorted list
# avoid using a second list, swap minimum element to first, second minimum to second position, ...
# time taken is O(n^2)

def selectionSort(seq):
    for start in range(len(seq)):
            minpos = start 
            for i in range(start, len(seq)):
                 if seq[minpos] > seq[i]:
                      minpos = i 
            seq[start], seq[minpos] = seq[minpos], seq[start]

# Insertion Sort
# start building a sorted sequence with one element
# pick up next unsorted element and insert it into its correct place in the already sorted sequence

def insertionSort(seq):
     for sliceEnd in range(len(seq)):
          pos = sliceEnd

          while pos > 0 and seq[pos] < seq[pos-1]:
               seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
               pos = pos - 1

# Recursion
# inductive functions
# define one or more base cases
# Inductive step defines f(n) in terms of smaller arguments

def insertionSortRecursion(seq):
    isort(seq, len(seq))

    def isort(seq, k):
        if k > 1:
            isort(seq, k - 1)
            insert(seq, k - 1)
    
    def insert(seq, k):
        pos = k
        while pos > 0 and seq[pos] < seq[pos - 1]:
             seq[pos], seq[pos - 1] = seq[pos - 1], seq[pos]
             pos = pos - 1
