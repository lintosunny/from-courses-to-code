# Introduction to Hash Tables

A hash table is a data structure that stores data using:

```text
Key → Value
```

pairs.

Python dictionaries are built using hash tables.

Example:

```python
{
    "nails": 1000,
    "screws": 800
}
```

- `"nails"` → key
- `1000` → value


# Address Space Concept

A hash table internally uses an address space.

Example:

```text
0 1 2 3 4 5 6 7
```

In implementation:
- this is usually a list/array



# How Hash Tables Work

A hash table uses:

```text
Hash Function
```

The hash function:
- takes a key
- converts it into an address/index



# Example

Key:

```text
"nails"
```

Hash function returns:

```text
2
```

So data gets stored at:

```text
Address 2
```

Example:

```text
Index 2 → ["nails", 1000]
```



# Key Idea

We use the key to calculate where the value should be stored.

This allows:
- very fast lookup



# Hash Function Characteristics

# 1. One-Way

Hashing works only one direction.

Example:

```text
"nails" → 2
```

But:

```text
2 → "nails"
```

is NOT possible.



# 2. Deterministic

Same input always gives same output.

Example:

```text
hash("nails") → 2
```

Every single time.

This is extremely important.



# Why Deterministic Matters

Suppose:

```python
get_item("nails")
```

If hashing is deterministic:
- we instantly know address is `2`

No searching needed.


# Hash Table Storage

Example list:

```text
0
1
2
3
4
5
6
7
```

Store:

```python
("nails", 1000)
```

Hash:

```text
"nails" → 2
```

Stored as:

```text
2 → [["nails", 1000]]
```



# Another Example

Store:

```python
("screws", 800)
```

Suppose hash gives:

```text
5
```

Store:

```text
5 → [["screws", 800]]
```


# Hash Collision

A collision happens when:

```text
Two different keys hash to same address
```

Example:

```text
"nails" → 2
"nuts"  → 2
```

Both want address `2`.



# Collision Problem

We cannot overwrite existing data.

Bad:

```text
2 → ["nuts", 1200]
```

because `"nails"` would be lost.



# Collision Handling Techniques

Two major methods:

1. Separate Chaining
2. Open Addressing



# 1. Separate Chaining

Store multiple key-value pairs at same address.

Example:

```text
2 →
[
  ["nails", 1000],
  ["nuts", 1200]
]
```

Usually implemented using:
- lists
- linked lists

This is the method used in this course.



# Separate Chaining Visualization

```text
Index 2:
[
   ["nails", 1000],
   ["nuts", 1200]
]
```

When searching:
- go to address
- loop through items



# Separate Chaining Using Linked Lists

Another version:

```text
2 → nails → nuts → paint
```

Need traversal inside chain.



# 2. Open Addressing

Instead of storing multiple items together:

Search for another empty address.



# Linear Probing

Most common open addressing technique.

Example:

```text
"nails" → 2
```

stored at:

```text
2
```

Now:

```text
"nuts" → 2
```

Collision occurs.

Move forward until empty slot found.

Example:

```text
2 → nails
3 → nuts
4 → paint
```



# Linear Probing Visualization

```text
0
1
2 → nails
3 → nuts
4 → paint
5
6
7
```



# Comparison of Collision Techniques

| Method | Idea |
|---|---|
| Separate Chaining | Multiple items per address |
| Open Addressing | Find another empty address |



# Hash Table Lookup

Suppose:

```python
get_item("bolts")
```

Hash:

```text
"bolts" → 6
```

Go directly to:

```text
Index 6
```

Retrieve value immediately.



# Why Hash Tables are Fast

Instead of searching through all items:

```text
O(n)
```

we directly jump to address.

Average lookup:

```text
O(1)
```



# Hash Table Big O

| Operation | Average Case |
|---|---|
| Insert | O(1) |
| Lookup | O(1) |
| Delete | O(1) |



# Worst Case Complexity

Worst case:

```text
All keys collide
```

Then lookup becomes:

```text
O(n)
```

because we may need to search chain.



# Hash Table vs List

## List Lookup

Need traversal:

```text
O(n)
```



## Hash Table Lookup

Direct address access:

```text
O(1)
```

Much faster.



# Python Dictionaries

Python dictionaries are implemented using:
- hash tables

Example:

```python
inventory = {
    "nails": 1000,
    "nuts": 1200
}
```



# Common Hash Table Uses

- Dictionaries
- Sets
- Caching
- Database indexing
- Fast lookups
- Counting frequency
- Duplicate detection


# Important Interview Patterns

## Frequency Counter

Example:

```python
counts[num] = counts.get(num, 0) + 1
```



## Fast Lookup

Use hash set:

```python
seen = set()
```

for:

```text
O(1)
```

membership checks.



# Important Interview Questions

- Two Sum
- Group Anagrams
- First Non-Repeating Character
- Contains Duplicate
- Longest Consecutive Sequence
- Subarray Sum



# Key Concepts to Remember

## Hash Function
Converts key into address.


## Deterministic
Same input → same output.



## One-Way
Cannot reverse hash.



## Collision
Two keys → same address.



## Separate Chaining
Multiple items at same address.



## Linear Probing
Find next empty slot.



# Main Idea of Hash Tables

Hash tables trade:

```text
Extra memory
```

for:

```text
Very fast lookup speed
```

Usually:

```text
O(1)
```