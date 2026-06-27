# ============================================================
# BUBBLE SORT
# ============================================================

# Bubble Sort compares adjacent elements and swaps them
# if they are in the wrong order.

# Example:
# [4, 2, 6, 5, 1, 3]
#
# Pass 1 -> Largest element (6) moves to the end
# Pass 2 -> Second largest element (5) moves to its position
# Continue until the list is sorted.

# Key Idea:
# - Compare neighboring elements
# - Swap if left > right
# - After each pass, the largest unsorted element
#   "bubbles up" to the end

# Comparisons per pass:
# n-1, n-2, n-3, ..., 1

# Time Complexity:
# Best:    O(n)   (optimized version)
# Average: O(n²)
# Worst:   O(n²)

# Space Complexity: O(1)

# Memory Trick:
# "Big numbers bubble to the top."
# ============================================================


def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

nums = [1, 2, 3, 5, 4]
print(f"Before sorting: {nums}")
print(f"After sorting: {bubble_sort(nums)}")