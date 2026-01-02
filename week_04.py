
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

