# name, value, type
# Names inherit their value from their current value (Dynamically type)
# Values have types, it determines what operations are allowed
# type(e) returns type of expression e, eg: int, float, bool
# Boolean values: True, False
# Logical operators (bool): not, and, or

print(5 > 10)  # returns Falase

# Strings
# Type string, str, a sequence of characters
# A single character is a str of length 1, no separate type char
# Enclose in quotes - single, double, or even triple
# position 0, 1, 2, ..., n-1 for a string of length n
# negative indexing, -1 returns the last index
# combine strings, operation +
# len(s) returns length of s
# slice is a segment of a string. s = 'hello', s[1:4] -> 'ell'
# s[i:j] starts at s[i] and ends at s[j-1]
# s[:j] starts at s[0], so s[0:j]
# s[i:] ends at s[len(s)-1], so s[i:len(s)]
# strings are immutable values, can't modify like s[2] = 'p', we have to use slices and concatenation

# Lists
# sequence of values, [1, 2, 3]
# type need not be uniform, ['a', 1, True]
# extract values by position, slice, like str
# str vs list, for a single position and slice str returns str, but in list a single position returns str and a slice returns a list
# Nested lists - list can contain other lists
# nested = [[2, [37]], 4, ["hello"]], nested[2][0][3] -> l
# unlike str list can be updated in place, like nested[1] = 7 possible, because lists are mutable
# important! mutable vs immutable
# values of type int, float, bool, str are immutable
# so, a = 1, b = a, a = 2, end a = 2 and b = 1
# list is immutable
# so, a = [1, 2], b = a, a[1] = 3, end a = [1, 3] and b = [1, 3]
# for mutable values assignment does not create a fresh copy, but for immutable it will create a fresh copy. That is why changes are reflecting in different ways
# then how can we create a copy of list without connected to the original one, list2 = list1[:], [:] = [0: len(n)]
# how to check x and y refering to memory location or object, x is y, then it will return True
# concatenation (+) this always produces a new list, list3 = list1 + list2, imp: concate will create a fresh copy, it won't be connected with the original one.

# control flow
# determines order which statements are executed
# shortcut conditions
# Numeric value 0 and empty sequences "", [] are treated as False, everything else is True
# Loops: repeated actions
# range(i,j) generates a sequence i, i+1, ..., j-1
# for i in n: repeat a fixed number of times
# Loops based on a condition, while: don't know number of repetations in advance

# Functions
# group of statements perform a given task and which can use repeatively from time to time
# return statement exits and return a value
def power(x, n):
    ans = 1
    for i in range(0, n):
        ans = ans * x
    return ans
    
# passing values to functions - argument value is substituted for name
# names in function have local scope
# recursion - function can call itself
def factorial(n):
    if n <= 0:
        return 1
    else:
        val = n * factorial(n-1)
        return val

# Example
def factors(n):
    f = []
    for i in range(1, n+1):
        if n % i == 0:
            f.append(i)
    return f

def isprime(n):
    return factors(n) == [1, n]
    
    
if __name__ == "__main__":
    print(factors(10))
    print(isprime(10))
    print(factors(3))
    print(isprime(3))
