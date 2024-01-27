# Sum of Integers >< 
# From 1 to N...go!  ? 
# Undefined <>
# math numbers --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Calculate sum of integers from 1 to given N (including).

# Input: Integer (int).
# Output: Integer (int).

# Examples:
assert sum_upto_n(1) == 1
assert sum_upto_n(2) == 3
assert sum_upto_n(3) == 6
assert sum_upto_n(4) == 10

# How it’s used: this function can be used in a variety 
# of mathematical and algorithmic contexts, such as in calculating 
# the nth triangular number, determining the cost for certain operations in algorithms, etc.

# Precondition:
# -    1 ≤ N ≤ 900.

# ___________________________________________________________________________________
# SOLUTION <>
import math

def sum_upto_n(N: int) -> int:
    return sum(range(1,N+1))
  
# <><><><><> Best "Clear" Solution <><><><><>
def sum_upto_n(N: int) -> int:
    return N*(N+1)//2

# <><><><><> Best "Speedy" Solution <><><><><>
def sum_upto_n(N: int) -> int:
    return sum([i for i in range(1, N+1)])

# <><><><><> Uncategorized <><><><><>

def sum_upto_n(N: int) -> int:
    liczba = 0
    for i in range(1,N+1):
        liczba += i
    return liczba

# ___________________________________________________________________________________
