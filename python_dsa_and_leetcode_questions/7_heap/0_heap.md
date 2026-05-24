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

---

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

---

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