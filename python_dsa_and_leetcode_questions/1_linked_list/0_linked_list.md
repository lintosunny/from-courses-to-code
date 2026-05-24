# Linked Lists - DSA Notes

# Introduction to Linked Lists

A linked list is a linear data structure where:
- Each item is stored in a separate node
- Each node points to the next node

Example:

```text
Head
 ↓
11 → 3 → 23 → 7 → None
                      ↑
                     Tail
```



# Linked List vs Python List

## Python List

Python lists:
- Have indexes
- Store elements in contiguous memory

Example:

```python
arr = [11, 3, 23, 7]
```

Memory looks like:

```text
[11][3][23][7]
```

All items are stored next to each other.



## Linked List

Linked lists:
- Do NOT have indexes internally
- Nodes are scattered in memory
- Connected using pointers

Memory looks like:

```text
[11] -> [3] -> [23] -> [7]
```

Each node knows where the next node is.



# Components of a Linked List

## Head

Points to first node.

```text
Head → 11
```



## Tail

Points to last node.

```text
7 → None
↑
Tail
```



## Node

Each node contains:
1. Value
2. Pointer to next node

Example node:

```text
[value | next]
```



# Linked List Visualization

```text
Head
 ↓
11 → 3 → 23 → 7 → None
                      ↑
                     Tail
```



# Why Lists Have O(1) Index Access

Python lists are contiguous in memory.

Example:

```text
Index 0 → Address A
Index 1 → Address A + 1
Index 2 → Address A + 2
```

This allows:

```python
arr[2]
```

to be:

```text
O(1)
```



# Why Linked Lists Do NOT Have O(1) Index Access

Linked lists are scattered in memory.

To reach index 2:

```text
Head → next → next
```

Need traversal.

Complexity:

```text
O(n)
```



# Linked List Big O

# Append to End

Example:

```text
11 → 3 → 23 → 7
```

Append `4`:

```text
11 → 3 → 23 → 7 → 4
```

Steps:
- Tail points to new node
- Update tail

Complexity:

```text
O(1)
```

Reason:
- Same number of operations regardless of list size



# Remove from End

Example:

```text
11 → 3 → 23 → 7
```

Remove `7`.

Problem:
- Need node before tail

Must traverse:

```text
11 → 3 → 23
```

Then:
- Set tail to `23`
- Remove `7`

Complexity:

```text
O(n)
```



# Add to Beginning

Example:

```text
4 → 11 → 3 → 23 → 7
```

Steps:
1. New node points to old head
2. Head moves to new node

Complexity:

```text
O(1)
```



# Remove from Beginning

Example:

```text
11 → 3 → 23 → 7
```

Remove `11`.

Steps:
1. Head moves to next node

```text
head = head.next
```

Complexity:

```text
O(1)
```


# Insert in Middle

Insert `4` after `23`.

Before:

```text
11 → 3 → 23 → 7
```

After:

```text
11 → 3 → 23 → 4 → 7
```

Need to:
1. Traverse to `23`
2. Adjust pointers

Complexity:

```text
O(n)
```

because traversal required.



# Remove from Middle

Remove `4`:

```text
11 → 3 → 23 → 4 → 7
```

becomes:

```text
11 → 3 → 23 → 7
```

Need to:
1. Traverse to node before target
2. Update pointer

Complexity:

```text
O(n)
```



# Lookup by Value

Find `23`.

Need to traverse:

```text
11 → 3 → 23
```

Complexity:

```text
O(n)
```



# Lookup by Index

Find index `2`.

Need traversal from head.

Complexity:

```text
O(n)
```

Unlike arrays:
- Linked lists do not support direct indexing



# Linked List vs List Big O

| Operation | Linked List | Python List |
|---|---|---|
| Append End | O(1) | O(1) |
| Remove End | O(n) | O(1) |
| Add Beginning | O(1) | O(n) |
| Remove Beginning | O(1) | O(n) |
| Lookup by Index | O(n) | O(1) |



# Linked Lists Under the Hood

A node is NOT just a value.

It contains:
- value
- next pointer



# Node Structure

Conceptually:

```python
{
    "value": 4,
    "next": None
}
```



# Example Linked List

```text
11 → 3 → 23 → 7
```

Can be imagined like:

```python
{
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}
```



# How Nodes Connect

Example:

```text
23 → 7
```

Means:

```python
23.next = 7
```

The `next` pointer stores reference to next node.



# Traversal Logic

To reach `23`:

```text
Head → next → next
```

Conceptually:

```python
head.next.next.value
```



# Important Concepts

## Linked List Characteristics

| Feature | Linked List |
|---|---|
| Dynamic Size | ✅ |
| Contiguous Memory | ❌ |
| Fast Front Insert/Delete | ✅ |
| Fast Index Access | ❌ |
| Uses Pointers | ✅ |



# Advantages of Linked Lists

- Efficient insertion/removal at beginning
- Dynamic size
- No memory shifting required



# Disadvantages of Linked Lists

- Slow searching
- No direct indexing
- Extra memory for pointers



# Common Types of Linked Lists

## Singly Linked List

```text
A → B → C
```

One-directional.



## Doubly Linked List

```text
A ⇄ B ⇄ C
```

Can move forward and backward.



## Circular Linked List

Last node points back to head.

```text
A → B → C
↑       ↓
└───────┘
```



# Common Interview Questions

- Reverse Linked List
- Detect Cycle
- Merge Two Lists
- Remove Nth Node
- Find Middle Node
- Linked List Cycle
- Palindrome Linked List



# Key Interview Tips

- Draw pointer changes
- Carefully track `next`
- Most bugs happen from pointer mistakes
- Use temp variables when changing pointers



# Important Mental Model

A linked list is:

```text
A chain of nodes connected using pointers
```

NOT:
- contiguous memory
- indexed structure

Traversal always starts from:
- `head`