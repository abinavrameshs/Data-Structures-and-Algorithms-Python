"""
Complexity = O(n) 
It runs n times, and it proportionally increases.
Linear complexity
"""
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

"""
Complexity = O(2n) = O(n)
We normally drop the constant
"""
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n) : 
        print(j)

print_items(10)

"""
COmplexity = O(n^2)
"""

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

"""
COmplexity = O(n^3)
We can simplify it as O(n^2)
"""


def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(10)


"""
Drop non-dominants 
------------------
If a code runs in O(n^2 + n) times, we can consider it as O(n^2).
We can drop the non-dominant term "n"

Complexity = O(n^2 + n)
We can simplify it as O(n^2)

"""


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

print_items(10)


"""
Complexity = O(1)
Most efficient Big O.. This is the most optimal code that we can make it.
"""
def print_items(n):
    return n + n + n


"""
Complexity = O(a+b)

"""
def print_items(a,b):
    for i in range(a):
        print(i)
    for i in range(b):
        print(i)

"""
Complexity = O(a*b)

"""
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)