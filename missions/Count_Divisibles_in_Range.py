# Count Divisibles in Range (simplified) >< 
# Let's jump over range ? 
# Elementary+ <>
# math numbers --
# ___________________________________________________________________________________
# Elementary+
# DE English FR PL UK ZH-HANS

# Given two integers, n and k, 
# the task is to count how many numbers between 1 and n (inclusive) are divisible by k.

# Input: Two integers (int).
# Output: Integer (int).

# Examples:
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3

# How it’s used: this function can be useful in number theory problems, statistical computations, and various other mathematical and practical scenarios where such a count is needed.

# Precondition:
# 1 <= k <= n <= 109.
# ___________________________________________________________________________________
# SOLUTION <>
def count_divisible(n: int, k: int) -> int:
    return n//k


print("Example:")
print(count_divisible(2, 1))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7

# <><><><><> Best "Clear" Solution <><><><><>
import math
def count_divisible(n: int, k: int) -> int:
    # your code here
    return math.trunc(n/k)

# <><><><><> Best "Creative" Solution <><><><><>
def count_divisible(n: int, k: int) -> int:
    return n / 2 if k == 2 else 1 if n == k else sum([1 if i % k == 0 else 0 for i in range(1, n + 1)])

# <><><><><> Uncategorized <><><><><>
def count_divisible(n: int, k: int) -> int:

    return int(n/k)

# ___________________________________________________________________________________
