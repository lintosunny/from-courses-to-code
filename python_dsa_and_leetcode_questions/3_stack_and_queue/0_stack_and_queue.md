# Stacks - DSA Notes

# Introduction to Stacks

A stack is a linear data structure that follows:

```text
LIFO
```

Meaning:

```text
Last In, First Out
```

The last item added is the first item removed.



# Tennis Ball Analogy

Imagine a can of tennis balls.

```text
Push:
   ○
```

Push another:

```text
   ○
   ○
```

Push another:

```text
   ○
   ○
   ○
```

You can only remove the ball from the top.

To access lower balls:
- Must remove top balls first

This is exactly how a stack works.



# Stack Operations

## Push

Add item to top of stack.

Example:

```text
Push 10
```

```text
Top
 ↓
10
```

Push 20:

```text
Top
 ↓
20
10
```



## Pop

Remove item from top.

Before:

```text
Top
 ↓
20
10
```

Pop:

```text
20 removed
```

After:

```text
Top
 ↓
10
```



# Stack Visualization

```text
Top
 ↓
30
20
10
```

Pop order:

```text
30 → 20 → 10
```



# Real-World Example: Browser Back Button

Suppose you visit:

```text
Facebook
YouTube
Instagram
Email
```

Internally browser stores:

```text
Top
 ↓
Email
Instagram
YouTube
Facebook
```

When you click Back:
- Email removed
- Go to Instagram

Click Back again:
- Instagram removed
- Go to YouTube

This is stack behavior.



# Stack Characteristics

| Feature | Stack |
|---|---|
| Order | LIFO |
| Insert | Top only |
| Remove | Top only |
| Access | Top only |



# Implementing a Stack

Two common ways:

1. Using List
2. Using Linked List



# Stack Using Python List

Python list can behave like a stack.

Example:

```python
stack = []

stack.append(10)   # push
stack.append(20)

stack.pop()        # pop
```



# Important: Use Correct End of List

## Good Side

Adding/removing at end:

```python
append()
pop()
```

Complexity:

```text
O(1)
```



## Bad Side

Adding/removing at beginning:

```python
insert(0, x)
pop(0)
```

Complexity:

```text
O(n)
```

because all items must shift/re-index.



# Why Beginning Operations are O(n)

Example:

```text
[10, 20, 30]
```

Remove first item:

```text
20 must move
30 must move
```

Everything shifts left.



# Stack Using Linked List

We can also implement stack using linked list.

Best implementation:

```text
Top
 ↓
10 → 20 → 30 → None
```

Add/remove from head side.



# Why This Direction is Better

With linked list:

## Add at beginning

```text
O(1)
```

## Remove at beginning

```text
O(1)
```



# Wrong Way to Build Stack

Bad design:

```text
10 → 20 → 30 → None
                 ↑
                Top
```

Removing from end requires traversal.

Complexity:

```text
O(n)
```



# Correct Stack Direction

Best approach:

```text
Top
 ↓
30 → 20 → 10 → None
```

Push/pop happen at beginning.

Both operations:

```text
O(1)
```



# Stack Operations with Linked List

## Push

Similar to linked list `prepend`.

Example:

Before:

```text
Top
 ↓
20 → 10
```

Push `30`:

```text
Top
 ↓
30 → 20 → 10
```

Complexity:

```text
O(1)
```



## Pop

Similar to linked list `pop_first`.

Before:

```text
Top
 ↓
30 → 20 → 10
```

Pop:

```text
30 removed
```

After:

```text
Top
 ↓
20 → 10
```

Complexity:

```text
O(1)
```



# Stack Terminology

| Operation | Meaning |
|---|---|
| Push | Add item |
| Pop | Remove item |
| Peek/Top | View top item |



# Stack Big O

| Operation | Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |



# Stack Under the Hood

## Using List

```python
stack = [10, 20, 30]
```

Top is last element:

```text
30
```



## Using Linked List

Each node points to next node.

Example:

```text
Top
 ↓
30 → 20 → 10 → None
```

Only top pointer needed.

Unlike linked list:
- no need for tail/bottom



# Common Uses of Stacks

- Browser history
- Undo/Redo
- Function call stack
- Expression evaluation
- Backtracking
- DFS (Depth First Search)
- Parentheses matching



# Stack Example: Parentheses Matching

Expression:

```text
((a+b) * c)
```

Push:
- `(`

Pop:
- `)`

If stack becomes invalid:
- parentheses mismatch



# Important Interview Problems

- Valid Parentheses
- Min Stack
- Reverse String
- Evaluate Postfix Expression
- Daily Temperatures
- Next Greater Element



# Key Interview Tips

- Think LIFO
- Push/pop should happen on same side
- Use stack when problem involves:
  - reversing
  - undo
  - nested structures
  - previous states



# Main Idea to Remember

A stack allows access to:

```text
ONLY the most recently added item
```

Everything below it is blocked until top items are removed.