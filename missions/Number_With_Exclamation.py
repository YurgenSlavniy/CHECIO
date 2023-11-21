# ___________________________________________________________________________________
# Number With Exclamation >< 
# Look, it's a Number! ? 
# Elementary <>
# math numbers --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# This function should take a non-negative integer
# as an input and return the factorial of that number.
# The factorial of a non-negative integer n is the product 
# of all positive integers less than or equal to n .

# example
# Input: Integer (int).
# Output: Integer (int).

# Examples:
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800

# How it’s used:

# -    in mathematical applications to calculate permutations and combinations;
# -    in algorithms to solve problems related to counting arrangements.

# Precondition:

# -    n ∈ N₀

# ___________________________________________________________________________________
# SOLUTION <>
import math

def factorial(n: int) -> int:
    return math.factorial(n)


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000
