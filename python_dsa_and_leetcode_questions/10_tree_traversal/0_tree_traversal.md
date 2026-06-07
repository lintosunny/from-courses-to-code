# Tree Traversal

## What is Tree Traversal?

Tree traversal is the process of visiting every node in a tree and collecting their values into a list.

Unlike a linked list, which is linear and can only be traversed in one direction, a tree can be traversed in multiple ways.

There are two main categories of tree traversal:

1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
   - Preorder
   - Postorder
   - Inorder



# Breadth-First Search (BFS)

## Overview

Breadth-First Search visits nodes level by level:

```text
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

Traversal Order:

```text
47 → 21 → 76 → 18 → 27 → 52 → 82
```



## BFS Algorithm

Use two lists:

- **Queue (Q)** → Stores entire nodes
- **Results** → Stores only node values

### Steps

1. Add the root node to the queue.
2. While the queue is not empty:
   - Remove the first node.
   - Add its value to the results list.
   - Add its left child (if it exists) to the queue.
   - Add its right child (if it exists) to the queue.
3. Return the results list.



## Example

### Initial State

```text
Queue   = [47]
Results = []
```

### Process 47

```text
Results = [47]
Queue   = [21, 76]
```

### Process 21

```text
Results = [47, 21]
Queue   = [76, 18, 27]
```

### Process 76

```text
Results = [47, 21, 76]
Queue   = [18, 27, 52, 82]
```

### Process Remaining Nodes

```text
Results = [47, 21, 76, 18, 27, 52, 82]
Queue   = []
```



## Interesting Property of BFS

If the BFS output is grouped by levels:

```text
47
21 76
18 27 52 82
```

It recreates the original tree structure.



# Depth-First Search (DFS)

DFS explores as far as possible down a branch before backtracking.

There are three common DFS traversals:

1. Preorder
2. Postorder
3. Inorder



# DFS - Preorder

## Rule

```text
Root → Left → Right
```

### Example Tree

```text
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

### Traversal

```text
47 → 21 → 18 → 27 → 76 → 52 → 82
```



## Preorder Process

1. Visit root.
2. Traverse left subtree.
3. Traverse right subtree.

### Visualization

```text
47
|
21
|
18
↑
27
↑
76
|
52
↑
82
```



# DFS - Postorder

## Rule

```text
Left → Right → Root
```

### Example Tree

```text
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

### Traversal

```text
18 → 27 → 21 → 52 → 82 → 76 → 47
```



## Postorder Process

For every node:

1. Go left.
2. Go right.
3. Write the node value.

### Example

#### Node 18

```text
Left?  No
Right? No
Write 18
```

#### Node 27

```text
Left?  No
Right? No
Write 27
```

#### Node 21

```text
Left done
Right done
Write 21
```

Continue the same process until the root node is written last.



# DFS - Inorder

## Rule

```text
Left → Root → Right
```

### Example Tree

```text
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

### Traversal

```text
18 → 21 → 27 → 47 → 52 → 76 → 82
```



## Inorder Process

For every node:

1. Go left.
2. Write node value.
3. Go right.

### Example

#### Node 18

```text
Left?  No
Write 18
Right? No
```

#### Node 21

```text
Left done
Write 21
Go right
```

Continue until all nodes are processed.



## Important Property of Inorder Traversal

For a **Binary Search Tree (BST)**, inorder traversal returns values in **sorted (ascending) order**.

Example:

```text
18 → 21 → 27 → 47 → 52 → 76 → 82
```

This is the numerical order of the values in the tree.



# Traversal Comparison

Given:

```text
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

| Traversal Type | Order |
|---------------|--------|
| Breadth First Search (BFS) | 47, 21, 76, 18, 27, 52, 82 |
| DFS Preorder | 47, 21, 18, 27, 76, 52, 82 |
| DFS Postorder | 18, 27, 21, 52, 82, 76, 47 |
| DFS Inorder | 18, 21, 27, 47, 52, 76, 82 |


# Quick Memory Tricks

### BFS

```text
Level by Level
```

### DFS Preorder

```text
Root → Left → Right
```

### DFS Postorder

```text
Left → Right → Root
```

### DFS Inorder

```text
Left → Root → Right
```

**Key Interview Tip:**  
For a Binary Search Tree (BST), **Inorder Traversal always produces a sorted sequence.**