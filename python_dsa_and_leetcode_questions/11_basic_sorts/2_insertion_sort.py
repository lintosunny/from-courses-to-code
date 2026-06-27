# ============================================================
# INSERTION SORT
# ============================================================
# 1. Start from the second element (index 1).
# 2. Compare the current element with previous elements.
# 3. Shift larger elements one position to the right.
# 4. Insert the current element into its correct position.
# 5. Repeat until all elements are processed.

# Time Complexity:
# Best   : O(n)    (Already sorted)
# Average: O(n²)
# Worst  : O(n²)   (Reverse sorted)

# Space Complexity: O(1)  (In-place sorting)
# ============================================================

def insertion_sort(my_list: list[int]) -> list[int]:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp 
            j -= 1
    return my_list

l = [2, 6, 3, 7, 4]
print(insertion_sort(l))