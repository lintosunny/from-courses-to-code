# Introduction to Sets

Sets are similar to dictionaries except that instead of having key/value pairs they only have the keys but not the values.

Like dictionaries, they are implemented using a hash table (which is why we are covering them here).

Sets can only contain unique elements (meaning that duplicates are not allowed).

They are useful for various operations such as finding the distinct elements in a collection and performing set operations such as union and intersection.

They are defined by either using curly braces `{}` or the built-in `set()` function like this:


## Creating Sets

```python
# Create a set using {}
my_set = {1, 2, 3, 4, 5}

# Create a set using set()
my_set = set([1, 2, 3, 4, 5])
```


## Common Set Operations

### Add an Element

```python
# Add an element to a set
# If the number 6 is already in the set it will not be added again.
my_set.add(6)
```



### Add Multiple Elements

```python
# Update is used to add multiple elements to the set at once.
# It takes an iterable object (e.g., list, tuple, set)
# as an argument and adds all its elements to the set.

# If any elements already exist in the set,
# they are not added again.
my_set.update([3, 4, 5, 6])
```



### Remove an Element

```python
# Removing an element from a set
my_set.remove(3)
```


## Set Operations

### Union of Two Sets

```python
other_set = {3, 4, 5, 6}

union_set = my_set.union(other_set)
```


### Intersection of Two Sets

```python
intersection_set = my_set.intersection(other_set)
```


### Difference Between Two Sets

```python
difference_set = my_set.difference(other_set)
```


## Membership Checking

```python
# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")
```


## Key Points About Sets

- Sets store only unique values
- Sets are unordered
- Sets are mutable (can be changed)
- Sets use hash tables internally
- Membership checking (`in`) is very fast


## Common Uses of Sets

- Removing duplicates
- Fast lookups
- Finding common elements
- Union and intersection operations
- Solving coding interview problems efficiently


Now let's look at some common coding interview questions that use sets!