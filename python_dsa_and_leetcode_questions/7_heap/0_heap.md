# Heaps - DSA Notes

# Introduction to Heaps

A heap is a special type of binary tree.

Example of a Max Heap:

```text
          99
        /    \
      72      61
     /  \    /  \
   58   55  38  18
```

It looks similar to a Binary Search Tree (BST), but the rules are different.



# Heap Property

## Max Heap

In a max heap:

```text
Parent >= Children
```

Every node is greater than or equal to all of its descendants.

This means:
- Largest value is always at the top (root)

Example:

```text
99 > 72, 61
72 > 58, 55
61 > 38, 18
```



## Min Heap

In a min heap:

```text
Parent <= Children
```

Smallest value is always at the top.

Example:

```text
          5
        /   \
      10     20
     / \    / \
   30 40  50 60
```



# Complete Binary Tree

A heap must always be a **complete binary tree**.

## What is a Complete Tree?

A tree is complete when:
- Every level is filled from left to right
- No gaps allowed

Valid:

```text
        10
       /  \
      8    6
     / \
    5   4
```

Invalid:

```text
        10
       /  \
      8    6
       \
        4
```

Gap exists on left side.



# Height of a Heap

For a complete binary tree:

```text
Height = log₂(n)
```

Example:

```text
8 nodes
log₂(8) = 3
```

So height is approximately `3`.

This is important for:
- Heap insertion
- Heap removal
- Time complexity



# Duplicates in Heaps

Unlike BSTs, heaps can contain duplicates.

Example:

```text
          99
        /    \
      99      61
```

This is still a valid heap.



# Important Heap Rule

Other than the root being largest (or smallest):

❌ No ordering guarantee exists.

Example:

Both are valid max heaps:

```text
        99
       /  \
     72    61
```

and

```text
        99
       /  \
     61    72
```

As long as:
- Parent ≥ children

the heap is valid.



# Heaps are NOT Good for Searching

Heap only guarantees:
- Largest item at top (max heap)
- Smallest item at top (min heap)

Searching inside heap is inefficient.

Main purpose:
- Quickly access/remove largest or smallest element



# Heap Storage

Huge difference from BST:

## BST
Stored using nodes and pointers.

## Heap
Stored using a list (array).

No node class required.



# Heap Stored in List

Example heap:

```text
          99
        /    \
      72      61
     /  \    /  \
   58   55  38  18
```

Stored as:

```python
heap = [99, 72, 61, 58, 55, 38, 18]
```

Level-by-level insertion:

```text
99
72 61
58 55 38 18
```



# Two Common Indexing Styles

## Style 1 (Most Common in Python)

Start at index `0`

```python
heap = [99, 72, 61, 58]
```



## Style 2 (Used for Easier Math)

Leave index `0` empty.

```python
heap = [None, 99, 72, 61, 58]
```

This makes parent/child calculations easier.

The transcript uses this method.



# Heap Visualization with Indexes

```text
Index:  1   2   3   4   5   6   7

Heap:  [99, 72, 61, 58, 55, 38, 18]
```

Tree:

```text
              99(1)
           /         \
       72(2)        61(3)
      /    \        /    \
   58(4) 55(5)  38(6) 18(7)
```



# Heap Math

# Finding Children

For a node at index `i`:

## Left Child

```text
2 × i
```

## Right Child

```text
2 × i + 1
```


# Example

Node:

```text
72 at index 2
```

Left child:

```text
2 × 2 = 4
```

Right child:

```text
2 × 2 + 1 = 5
```

Children are:
- index 4 → 58
- index 5 → 55



# Another Example

Node:

```text
61 at index 3
```

Left child:

```text
2 × 3 = 6
```

Right child:

```text
2 × 3 + 1 = 7
```

Children:
- index 6 → 38
- index 7 → 18



# Finding Parent

For a node at index `i`:

```text
Parent = i // 2
```

(`//` means integer division)



# Example

Node at index `6`:

```text
6 // 2 = 3
```

Parent is at index `3`.



Another example:

```text
7 // 2 = 3
```

(3.5 becomes 3 because integer division removes decimals)

Parent of index `7` is also index `3`.



# Why Leave Index 0 Empty?

Leaving index `0` empty makes formulas cleaner:

| Operation | Formula |
|---|---|
| Left child | `2 × i` |
| Right child | `2 × i + 1` |
| Parent | `i // 2` |

Very simple calculations.


# Key Characteristics of Heaps

| Feature | Heap |
|---|---|
| Binary Tree | ✅ |
| Complete Tree | ✅ |
| Sorted | ❌ |
| Duplicates Allowed | ✅ |
| Fast Root Access | ✅ |
| Good for Searching | ❌ |



# Main Uses of Heaps

- Priority Queue
- Scheduling systems
- Task management
- Dijkstra’s Algorithm
- Heap Sort
- Finding largest/smallest efficiently


# Important Interview Concepts

## Max Heap
Largest item on top.

## Min Heap
Smallest item on top.

## Heap Height

```text
O(log n)
```

because heap is a complete binary tree.


# Time Complexity Preview

| Operation | Complexity |
|---|---|
| Insert | O(log n) |
| Remove Root | O(log n) |
| Access Root | O(1) |
| Search | O(n) |

(These are covered later in priority queues and heap operations.)


# Priority Queues and Heaps

## What is a Priority Queue?

A **Priority Queue** is a data structure where elements are removed based on their priority rather than the order in which they were added.

For a **Max Priority Queue**, the element with the highest value has the highest priority and is removed first.

Example:

```
95, 75, 50, 60, 30
```

The first element removed would be `95`.



## Why Use a Heap for a Priority Queue?

A **Heap** is the most efficient data structure for implementing a priority queue because:

- The highest-priority element is always at the root.
- Insertion is efficient.
- Removal is efficient.
- The tree remains balanced.

For a Max Heap:

```
        95
       /  \
     75    60
    / \    /
   50 30 40
```

The maximum value (`95`) is always at the top.



## Alternative Implementations

### 1. Linked List

A priority queue can be implemented using a linked list.

To remove the highest-priority element:

1. Traverse the entire list.
2. Find the maximum value.
3. Remove it.

### Time Complexity

| Operation | Complexity |
|------------|------------|
| Find Max | O(n) |
| Remove Max | O(n) |
| Insert | O(1) |

**Problem:** Requires scanning the entire list to find the highest value.



### 2. Unsorted Array/List

Example:

```python
[50, 95, 30, 75, 60]
```

Since values are randomly placed, finding the maximum requires checking every element.

### Time Complexity

| Operation | Complexity |
|------------|------------|
| Find Max | O(n) |
| Remove Max | O(n) |
| Insert | O(1) |

**Problem:** Inefficient for repeated maximum lookups.



### 3. Dictionary (Hash Table)

A dictionary provides O(1) lookup if the key is known.

Example:

```python
{
    "a": 50,
    "b": 95,
    "c": 30
}
```

However, if we need the highest value:

- Every value must still be examined.

### Time Complexity

| Operation | Complexity |
|------------|------------|
| Find Max | O(n) |

**Problem:** Fast lookup does not help when searching for the largest value.



### 4. Binary Search Tree (BST)

In a balanced BST:

```
       50
      /  \
    30    75
          \
           95
```

The largest value is found by traversing right.

### Balanced BST

| Operation | Complexity |
|------------|------------|
| Insert | O(log n) |
| Remove Max | O(log n) |



### Problem with BSTs

BSTs are not always balanced.

Example:

```
50
  \
   75
     \
      95
```

This behaves like a linked list.

### Worst Case

| Operation | Complexity |
|------------|------------|
| Insert | O(n) |
| Remove Max | O(n) |



## Why Heaps Are Better

A Heap is always a **complete binary tree**, meaning it remains balanced.

Example:

```
        95
       /  \
     75    60
    / \    /
   50 30 40
```

When removing the root:

1. Move the last element to the root.
2. Sink it down until heap property is restored.

The maximum distance an element can move is the **height of the tree**.

For a balanced binary tree:

```
Height = O(log n)
```



## Heap Operations

### Insert

1. Add element to the next available position.
2. Bubble it up until heap property is satisfied.

**Time Complexity:** O(log n)



### Remove Maximum

1. Remove root.
2. Move last element to root.
3. Sink it down.

**Time Complexity:** O(log n)



## Why O(log n) Is So Efficient

Suppose a priority queue contains:

```
1,000,000 elements
```

### O(n)

Requires:

```
1,000,000 operations
```

### O(log₂ n)

```
log₂(1,000,000) ≈ 20
```

Requires only about:

```
20 operations
```

This is dramatically more efficient than scanning all elements.



## Complexity Comparison

| Data Structure | Insert | Remove Max |
|---------------|---------|------------|
| Linked List | O(1) | O(n) |
| Unsorted Array | O(1) | O(n) |
| Dictionary | O(1) lookup | O(n) to find max |
| Balanced BST | O(log n) | O(log n) |
| Unbalanced BST | O(n) | O(n) |
| Heap | O(log n) | O(log n) |



## Key Takeaways

- A Priority Queue removes elements based on priority.
- Heaps are the preferred implementation for Priority Queues.
- Heaps keep the highest-priority element at the root.
- Heap insertion and removal both run in **O(log n)** time.
- Because heaps remain balanced, they avoid the worst-case behavior of Binary Search Trees.
- For large datasets, heaps are significantly more efficient than linked lists, arrays, or hash tables when repeatedly retrieving the highest-priority element.