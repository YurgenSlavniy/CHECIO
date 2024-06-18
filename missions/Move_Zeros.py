# Move Zeros >< 
# Move all zeros in a list to the end of it ? 
# Elementary+ <>
# list --
# ___________________________________________________________________________________
# Elementary+

# You are given a list of integers. 
# Move all zeros in the list to the end of it. 
# The order of non-zero elements should not change.

# Input: A list of integers.
# Output: A list or another Iterable (tuple, genenator, iterator) of integers.

# Examples:
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

# ___________________________________________________________________________________
# SOLUTION <>
from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:
    new_items = []
    zeros = []
    for el in items:
        if el == 0:
            zeros.append(el)
        else:
            new_items.append(el)
            
    return new_items + zeros


print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
