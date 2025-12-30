# way 1: find the gratest common divisor
def gcd(m: int, n: int) -> int:

    l = min(m, n)

    for i in range(1, l+1):
        if m % i == 0 and n % i == 0:
            k = i

    return k


# way 2: scan backward
def gcd_backward(m: int, n: int) -> int:
    
    l = min(m, n)

    while l > 0:
        if m%l == 0 and n%l == 0:
            return l 
        else:
            l -= 1


# way 3: recursion + euclid's algorithm
def gcd_rec(m: int, n: int) -> int:
    # assume m >= n
    if m < n:
        (m,n) = (n,m)
    
    if m%n == 0:
        return n 
    else:
        diff = m-n 
        return(gcd(max(n, diff), min(n, diff)))


# way 4: while + euclid's algorithm
def gcd_while(m: int, n: int) -> int:
    # assume m >= n
    if m < n:
        (m,n) = (n,m)
    
    if m%n == 0:
        return n 
    
    while m%n != 0:
        diff = m-n 
        (m,n) = (max(n, diff), min(n, diff))
    
    return n


# way 5: euclid's algorithm + better approach
def gcd_final(m: int, n: int) -> int:
    # assume m >= n
    if m < n:
        (m,n) = (n,m)
    
    if m%n == 0:
        return n 
    
    if m%n == 0:
        return n 
    else:
        return gcd(n, m%n)


if __name__ == "__main__":
    x = gcd_final(18, 24)
    print(x)