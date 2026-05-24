# Graphs - DSA Notes

# Introduction to Graphs

A graph is a data structure made up of:

- **Vertices (Nodes)**
- **Edges (Connections)**

Example:

```text
A ----- B
 \     /
   \ /
    C
```

- Proper term: **Vertex**
- Common term: **Node**
- Plural: **Vertices**

The connections between vertices are called:

- Proper term: **Edges**
- Common term: **Connections**

A vertex can connect to many other vertices.

---

# Weighted Graphs

Sometimes edges have a **weight** or **cost**.

Example:

```text
A --5-- B
A --15-- C
```

Used in:
- Google Maps
- GPS Routing
- Network Routing

Example:
- One route may have fewer hops
- Another route may take less time because traffic is lower

So shortest path is not always best path.


# Directional vs Bidirectional Graphs

## Bidirectional Graph

Connection works both ways.

Example:
- Facebook friendship

```text
A ----- B
```

Meaning:
- A connected to B
- B connected to A

Usually drawn without arrows.


## Directional Graph

Connection works one way.

Example:
- Twitter / Instagram follow

```text
A -----> B
```

Meaning:
- A follows B
- B may not follow A


# Trees and Linked Lists are Graphs

## Tree
A tree is a type of graph with restrictions.

Binary tree:
- Each node can connect to at most 2 nodes


## Linked List
Linked list is also a graph.

Restriction:
- Each node points to only one next node


# Graph Representation

Two common ways:

1. Adjacency Matrix
2. Adjacency List


# Adjacency Matrix

A graph can be represented using a 2D matrix.

Example graph:

```text
A ----- B
|       |
E ----- D
 \     /
    C
```

Matrix representation:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 0 | 1 |
| B | 1 | 0 | 1 | 0 | 0 |
| C | 0 | 1 | 0 | 1 | 0 |
| D | 0 | 0 | 1 | 0 | 1 |
| E | 1 | 0 | 0 | 1 | 0 |


## Matrix Rules

### 1. Self-connections are usually 0

```text
A → A = 0
```

So diagonal is usually all zeros.


### 2. Bidirectional Graphs are Symmetrical

If:

```text
A ↔ B
```

Then:

```text
matrix[A][B] = 1
matrix[B][A] = 1
```

Matrix becomes symmetric across diagonal.


### 3. Directed Graphs Break Symmetry

If:

```text
A → B
```

but NOT:

```text
B → A
```

Then:

```text
matrix[A][B] = 1
matrix[B][A] = 0
```


# Weighted Adjacency Matrix

Instead of storing `1`, store weight.

Example:

```text
A --5-- B
```

Store:

```text
matrix[A][B] = 5
```


# Adjacency List

Most common graph representation in interviews.

Represent graph using dictionary.

Example:

```python
graph = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "E"],
    "E": ["A", "D"]
}
```

Meaning:
- A connected to B and E
- B connected to A and C


# Why Adjacency List is Better

Adjacency matrix stores:
- Connections (`1`)
- Non-connections (`0`)

Most graphs are sparse:
- Few actual connections
- Huge number of zeros

Adjacency list stores only actual edges.

Much more memory efficient.


# Graph Big O

# Space Complexity

## Adjacency Matrix

```text
O(V²)
```

Because every vertex stores relationship with every other vertex.


## Adjacency List

```text
O(V + E)
```

Where:
- V = Vertices
- E = Edges

Much more efficient.


# Operations Big O

| Operation | Adjacency Matrix | Adjacency List |
|---|---|---|
| Add Vertex | O(V²) | O(1) |
| Add Edge | O(1) | O(1) |
| Remove Edge | O(1) | O(E) |
| Remove Vertex | O(V²) | O(V + E) |


# Add Vertex

## Matrix

Need to:
- Add new row
- Add new column

Essentially rebuild matrix.

Complexity:

```text
O(V²)
```


## List

Simply add new key:

```python
graph["F"] = []
```

Complexity:

```text
O(1)
```


# Add Edge

## Matrix

```text
matrix[A][B] = 1
```

Complexity:

```text
O(1)
```


## List

Append values:

```python
graph["A"].append("B")
graph["B"].append("A")
```

Complexity:

```text
O(1)
```


# Remove Edge

## Matrix

Set values to 0.

```text
matrix[A][B] = 0
```

Complexity:

```text
O(1)
```


## List

Need to search edge list.

Complexity:

```text
O(E)
```


# Remove Vertex

## Matrix

Need to:
- Remove row
- Remove column

Rebuild matrix.

Complexity:

```text
O(V²)
```


## List

Need to:
- Remove key
- Remove references from all neighbors

Complexity:

```text
O(V + E)
```


# Why Matrices Become Impractical

Imagine:
- Facebook has 1 billion users

Adjacency matrix would need:

```text
1 billion × 1 billion
```

entries.

Most entries are zeros because:
- Each user connects to only small fraction of users.

Huge memory waste.

Adjacency list avoids storing all those zeros.


# Key Takeaways

## Adjacency Matrix
### Pros
- Fast edge lookup
- Simple concept

### Cons
- Huge memory usage
- Expensive vertex operations


## Adjacency List
### Pros
- Memory efficient
- Easier to work with
- Preferred in interviews

### Cons
- Removing edges slower


# Most Important Interview Point

In DSA interviews:

✅ Use adjacency list unless specifically asked otherwise.

Most graph problems use:

```python
graph = {
    node: [neighbors]
}
```

representation.