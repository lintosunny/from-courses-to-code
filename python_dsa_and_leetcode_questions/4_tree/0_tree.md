# Introduction to Trees

A tree is a hierarchical data structure made of nodes connected together.

Example:

```text
        11
       /  \
      4    23
```



# Linked List is a Type of Tree

A linked list is actually a tree that never forks.

Example:

```text
11 → 4 → 23 → 7
```

It is a tree where:
- each node points to only one next node



# Binary Tree Node Structure

A binary tree node contains:

```text
[value | left | right]
```

Example node:

```python
{
    "value": 11,
    "left": None,
    "right": None
}
```



# Binary Tree

In a binary tree:
- each node can point to at most 2 children

Example:

```text
        11
       /  \
      4    23
```



# Trees are NOT Limited to Two Children

A tree can:
- point to 3 nodes
- 10 nodes
- unlimited nodes

But a **binary tree** specifically allows:
- maximum 2 children



# Tree Terminology

# Parent

A node that points to other nodes.

Example:

```text
        11
       /  \
      4    23
```

`11` is parent of:
- `4`
- `23`



# Child

Nodes connected below parent.

Example:
- `4` and `23` are children of `11`



# Siblings

Nodes sharing same parent.

Example:

```text
4 and 23
```

are siblings.


# Leaf Node

A node with no children.

Example:

```text
4
23
```

are leaf nodes.



# Important Tree Rule

A node can only have ONE parent.

If a node has multiple parents:

❌ it is NOT a tree



# Full Binary Tree

A tree is full when every node has:

- either 0 children
- or 2 children

Valid full tree:

```text
        11
       /  \
      4    23
```

Invalid full tree:

```text
        11
       /
      4
```

because node has only one child.



# Perfect Binary Tree

A tree is perfect when:
- every level is completely filled

Example:

```text
          11
        /    \
       4      23
      / \    / \
     1   6  18  30
```



# Complete Binary Tree

A tree is complete when:
- filled from left to right
- no gaps allowed

Valid complete tree:

```text
        11
       /  \
      4    23
     /
    1
```

Invalid complete tree:

```text
        11
       /  \
      4    23
       \
        1
```

Gap exists on left side.



# Relationship Between Tree Types

```text
Perfect Tree → Full Tree → Complete Tree
```

A perfect tree is also:
- full
- complete



# Binary Search Tree (BST)

A BST is a binary tree with ordering rules.



# BST Rules

For every node:

```text
Left side  < Parent
Right side > Parent
```



# BST Example

```text
          47
        /    \
      21      76
        \    /  \
        27  52  82
       /
      18
```



# BST Insertion Logic

Start from root.

## If value is smaller
Go left.

## If value is greater
Go right.

Repeat until empty spot found.



# Example: Insert 52

Start at:

```text
47
```

52 > 47 → go right

Compare with:

```text
76
```

52 < 76 → go left

Insert there.



# Example: Insert 18

18 < 47 → left

18 < 21 → left

Insert there.



# Important BST Property

For ANY node:

```text
All values on left are smaller
All values on right are greater
```



# BST Height and Logarithms

Perfect tree levels:

| Level | Approx Nodes |
|---|---|
| 1 | 2¹ |
| 2 | 2² |
| 3 | 2³ |
| 4 | 2⁴ |

Tree height grows as:

```text
log₂(n)
```



# Why BST Operations are Fast

BST uses:

```text
Divide and Conquer
```


# Example Search

Search for `49`.

Start:

```text
47
```

49 > 47 → go right

Half tree eliminated.

Compare:

```text
76
```

49 < 76 → go left

Half remaining tree eliminated.

Continue until found.



# BST Big O

# Average Case

| Operation | Complexity |
|---|---|
| Lookup | O(log n) |
| Insert | O(log n) |
| Remove | O(log n) |

Very efficient.



# Worst Case BST

Bad tree:

```text
11
  \
   23
     \
      47
        \
         91
```

Tree becomes linked list.

Search for `91`:

```text
11 → 23 → 47 → 91
```

Complexity:

```text
O(n)
```



# Important BST Note

Technically BST worst-case is:

```text
O(n)
```

But normally we assume reasonably balanced trees.

So BST is generally treated as:

```text
O(log n)
```



# Divide and Conquer Visualization

Searching `49`:

```text
          47
        /    \
      21      76
             /
           52
          /
        49
```

Step 1:
- eliminate left half

Step 2:
- eliminate half again

This repeated halving creates:

```text
O(log n)
```



# BST vs Linked List

| Operation | BST | Linked List |
|---|---|---|
| Lookup | O(log n) | O(n) |
| Insert | O(log n) | O(1) |
| Remove | O(log n) | O(n) |



# Why Linked List Insert is Faster

Linked list insertion:

```text
Append to end
```

No searching needed.

Complexity:

```text
O(1)
```



# Why BST Lookup is Faster

BST removes half the search space each step.

Linked list requires sequential traversal.



# Choosing the Right Data Structure

## Use Linked List When:
- insertion speed matters most
- many writes
- few lookups

Example:
- burst data ingestion



## Use BST When:
- fast searching needed
- fast retrieval important



# BST vs Python List

| Operation | BST | Python List |
|---|---|---|
| Insert End | O(log n) | O(1) |
| Lookup Value | O(log n) | O(n) |
| Remove Value | O(log n) | O(n) |
| Lookup Index | ❌ | O(1) |



# Important Interview Concepts

## BST Traversal Types

### DFS Traversals
- Preorder
- Inorder
- Postorder

### BFS Traversal
- Level Order



# Key Interview Problems

- Validate BST
- Lowest Common Ancestor
- Kth Smallest Element
- Invert Binary Tree
- Balanced Tree
- Maximum Depth
- Serialize/Deserialize Tree



# Key Takeaways

## Binary Tree
- max 2 children

## Full Tree
- 0 or 2 children

## Perfect Tree
- every level filled

## Complete Tree
- filled left to right

## BST
- ordered binary tree

## BST Advantage
- fast lookup using divide & conquer

## BST Weakness
- can degrade to linked list