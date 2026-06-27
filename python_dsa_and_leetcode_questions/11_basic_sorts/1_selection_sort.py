# ============================================================
# SELECTION SORT
# ============================================================
# 1. Assume the current index has the minimum value (min_index = i).
# 2. Compare it with all remaining elements.
# 3. Update min_index if a smaller element is found.
# 4. After the scan, swap only if min_index != i.
# 5. The current position is now sorted.
# 6. Repeat for the next index until the second-last element.

# Time Complexity:
# Best   : O(n²)
# Average: O(n²)
# Worst  : O(n²)

# Space Complexity: O(1)  (In-place sorting)
# ============================================================

def selection_sort(my_list: list[int]) -> list[int]:
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j 
        if i != min_index:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
    return my_list

l = [10, 2, 3, 6, 5, 9, 8]
print(selection_sort(l))