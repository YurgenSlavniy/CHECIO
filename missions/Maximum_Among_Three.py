# Maximum Among Three >< 
# There are three of us...one must remains. ? 
#  <>
# numbers--
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Given three integers, determine which one is the largest.

# Input: Three integers (int).
# Output: Integer (int).

# Examples:
assert max_of_three(1, 2, 3) == 3
assert max_of_three(3, 2, 1) == 3
assert max_of_three(1, 3, 2) == 3
assert max_of_three(0, 0, 0) == 0

# How it’s used: 
# - this function can be used in various algorithms 
# and computations where the highest value among multiple options needs to be selected.

# Precondition:

# -    -109 <= a, b, c <= 109.
 
 __________________________________________________________________________________
# SOLUTION <>
def max_of_three(a: int, b: int, c: int) -> int:
    return max([a,b,c])

print("Example:")
print(max_of_three(1, 2, 3))

# These "asserts" are used for self-checking
assert max_of_three(1, 2, 3) == 3
assert max_of_three(3, 2, 1) == 3
assert max_of_three(1, 3, 2) == 3
assert max_of_three(0, 0, 0) == 0
assert max_of_three(-1, -2, -3) == -1
assert max_of_three(5, 5, 4) == 5
assert max_of_three(-5, -5, -6) == -5
assert max_of_three(10, 9, 10) == 10
assert max_of_three(123, 456, 789) == 789
assert max_of_three(789, 123, 456) == 789

# <><><><><> Best "Clear" Solution <><><><><>
# Using the built-in function max instead of making a new one.
max_of_three = max

# <><><><><> Best "Creative" Solution <><><><><>
def max_of_three(a: int, b: int, c: int) -> int:
    # your code here
    return max(a,b,c)

# <><><><><> Uncategorized <><><><><>
def max_of_three(a: int, b: int, c: int) -> int:
    # your code here
    arr = [a, b, c]
    iterator = iter(arr)
    max_val = None
    try:
        while True:
            temp = next(iterator)
            if max_val is None:
                max_val = temp
            elif max_val < temp:
                max_val = temp
            elif max_val > temp:
                continue
            else:
                raise StopIteration
    except StopIteration:
        return max_val


# ___________________________________________________________________________________
