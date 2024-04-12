# Sort Except Zero >< 
# Zeros should not be changed ? 
# Simple <>
# list math --
# ___________________________________________________________________________________
# Simple
# DE English FR PL UK ZH-HANS

# Sort the integers in sequence in sequence. But the position of zeros should not be changed.

# Input: List of integers (int).
# Output: List or another Iterable (tuple, generator, iterator) of integers (int).

# Examples:
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]

# Precondition:
# All numbers are non-negative.
# ___________________________________________________________________________________
# SOLUTION <>
from collections.abc import Iterable

def except_zero(items: list[int]) -> Iterable[int]:
    zeros = [num for num in items if num == 0]
    non_zeros = sorted([num for num in items if num != 0])
    
    result = []
    zero_index = 0
    for num in items:
        if num == 0:
            result.append(0)
            zero_index += 1
        else:
            result.append(non_zeros.pop(0))
    return result

print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
