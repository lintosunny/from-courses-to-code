# Recursion

## What is Recursion?

Recursion is a programming technique where a **function calls itself**.

A simple definition:

> **Recursion is a function that calls itself... until it doesn't.**

Recursion can be difficult to understand at first and often requires reviewing multiple times before it fully clicks.

---

# Gift Box Analogy

A common way to understand recursion is through a gift box example.

Imagine you have a gift box that needs to be opened.

### Rules

* Use the `openGiftBox()` function to open a box.
* Inside the box, you may find:

  * A **ball** (the item you're looking for), or
  * Another **smaller gift box**.

If you find another gift box, you use the same `openGiftBox()` function again.

### Example

```
Gift Box
 └── Gift Box
      └── Gift Box
           └── Ball
```

Process:

1. Open the first box.
2. If it's another box, open it.
3. Repeat the same process.
4. Eventually, find the ball.
5. Stop.

---

# Pseudocode Example

```text
function openGiftBox():

    if ball:
        return ball

    openGiftBox()
```

### How it Works

* If the box contains a ball:

  * Return the ball.
  * Stop the function.

* Otherwise:

  * Open the smaller gift box.
  * The function calls itself.

---

# Important Characteristics of Recursion

## 1. The Process Must Stay the Same

Every recursive call performs the same action.

In the gift box example:

* Open box
* Check contents
* Repeat if necessary

The logic never changes.

---

## 2. The Problem Must Become Smaller

Each recursive call should move closer to a solution.

In the gift box example:

* Every new box is smaller than the previous one.
* Eventually, there are no more boxes left to open.

Without making progress toward a solution, recursion will never end.

---

# Understanding Recursive Calls

Suppose we have:

```
Box 1
 └── Box 2
      └── Box 3
           └── Ball
```

Execution:

### Call #1

```text
openGiftBox()
```

* Not a ball
* Calls itself

### Call #2

```text
openGiftBox()
```

* Not a ball
* Calls itself

### Call #3

```text
openGiftBox()
```

* Ball found
* Return ball

At this point, recursion stops because of the `return` statement.

---

# Base Case and Recursive Case

Every recursive function must have two parts.

## Base Case

The condition that stops recursion.

Example:

```text
if ball:
    return ball
```

When the ball is found, the function stops calling itself.

### Gift Box Example

```
Box → Box → Ball
             ↑
        Base Case
```

---

## Recursive Case

The condition where the function continues calling itself.

Example:

```text
openGiftBox()
```

Whenever another box is found, recursion continues.

### Gift Box Example

```
Box → Box → Ball
 ↑      ↑
Recursive Cases
```

---

# Why the Base Case is Critical

Without a base case:

```text
function openGiftBox():
    openGiftBox()
```

The function keeps calling itself forever:

```text
openGiftBox()
    openGiftBox()
        openGiftBox()
            openGiftBox()
                ...
```

This eventually causes a:

## Stack Overflow

A stack overflow occurs when too many function calls are placed on the call stack and memory is exhausted.

---

# Common Cause of Stack Overflow

## Base Case Never Becomes True

Example:

```text
if 1 > 2:
    return ball

openGiftBox()
```

Since:

```text
1 > 2
```

is always false, the recursion never stops.

The function continues forever until a stack overflow occurs.

### Debugging Tip

If a recursive function causes a stack overflow:

* Check whether the base case can actually become true.
* Ensure the problem gets smaller with each recursive call.

---

# Why a Return Statement is Important

Incorrect example:

```text
if ball:
    print("Hello World")

openGiftBox()
```

Even when the ball is found:

1. `"Hello World"` is printed.
2. Execution continues.
3. `openGiftBox()` is called again.

Result:

* Infinite recursion
* Stack overflow

### Correct Version

```text
if ball:
    return ball
```

A `return` statement immediately exits the current function call and prevents further recursion.

---

# Recursion Checklist

Before writing a recursive function, ensure:

✅ A base case exists.

✅ The base case will eventually become true.

✅ Each recursive call makes the problem smaller.

✅ A return statement stops execution when the base case is reached.

---

# Key Takeaways

* Recursion is a function calling itself.
* Every recursive function needs:

  * A **Base Case** (stopping condition)
  * A **Recursive Case** (calls itself again)
* The problem must become smaller with each call.
* Missing or unreachable base cases lead to stack overflow.
* A `return` statement is usually required to stop recursion correctly.
* The gift box analogy is a simple way to visualize how recursion works.

> Think of recursion as repeatedly opening smaller gift boxes until you finally find the item you're looking for.
