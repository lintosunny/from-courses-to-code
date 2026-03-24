
# selection sort and insertion sort are both O(n^2)\
# O(n^2) is infeasible for n over 5000
# Merge sort
# divide and conquer
# break it into 2 equal parts and then sort then merge, also using recursion
# time taken is O(n log n)
# Extra storage can be costly, merging A and B creates a new array C
# Inherently recursive, recursive call and return are expensive

def merge(A, B):
    C, m, n = [], len(A), len(B)
    i, j = 0, 0
    while i + j < m + n:
        if i == m:
            C.append(B[j])
            j = j + 1
        elif j == n:
            C.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j + 1
    return C

def mergeSort(A, left, right):
    if right - left <= 1:
        return A[left:right]
    if right - left > 1:
        mid = (left+right)//2
        L = mergeSort(A, left, mid)
        R = mergeSort(A, mid, right)
        return merge(L,R)
    
# Quick sort
# divide and conquer without merging
# time needed is O(n log n)
# choose a pivot element, typically the first value in the array
# partition A into lower and upper parts with respect to pivot, lesser than A and grater than A
# sorted array is worst case for quick sort O(n^2)- limited
# average case is O(n log n)
# merge sort is stable but quick sort is not stable, because we are destroying the original sort

def quickSort(A, l, r):
    if r - l <= 1:
        return ()
    
    yellow = l + 1

    for green in range(l+1, r):
        if A[green] <= A[l]:
            A[yellow], A[green] = A[green], A[yellow]
            yellow = yellow + 1
    
    # move pivot into place
    A[l], A[yellow - 1] = A[yellow - 1], A[l]

    quickSort(A, l, yellow - 1)
    quickSort(A, yellow, r)

# Tuples
# (age, name, primes) = (23, "linto", [3, 5])
# can assign a tuple of values to a name. x = (1, 2, 3)
# to extract positions and slice tuple behave same as list. tuple[0]
# tuples are immutable

# Dictionaries
# allows keys other than range(0, n)
# any immutable value can be key (it can be int, float, bool, string, tuple and not lists or dictionaries)
# can update dictionaries in place - mutable, like lists
# empty dictionary is {}
# can have nested dictionaries
# d = {}
# d.keys - returns keys of dict
# d.values - returns values in a dict
# dictionaries allow a flexible association of values to keys

# passing values to functions
# default value is provided in function definition, if this is omitted default value used
# default values are identified position, must come at end. order is important
# can pass function inside functions. 
# functions definitions behave like other assignments of values to names

# List comprehension
# [square(x) for i in range(100) if iseven(x)]
# ---map--- | ---generator----- | ---filter---

[(x, y, z) for x in range(100) for y in range(100) for z in range(100) if x*x + y*y == z*z]

# map and filter very useful functions to manipulate lists
# list comprehension provides a useful notation for combining map and filter
