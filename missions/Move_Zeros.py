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
def move_zeros(items: list[int]) -> list[int]:
    return [v for v in items if v] + [0] * items.count(0)


# <><><><><> Best "Creative" Solution <><><><><>
move_zeros = __import__('functools').partial(sorted, key=bool, reverse=True)


# <><><><><> Best "Speedy" Solution <><><><><>
def move_zeros(items: list[int]) -> list[int]:
    a, b = [],[]
    for j in items:
        if j :
            a.append(j)
        else:
            b.append(j)
    return a + b


# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def move_zeros(items: list[int]) -> list[int]:
    items2 = [i for i in items if i != 0]
    
    return np.hstack([items2,np.zeros(len(items)-len(items2), int)]).tolist()


# <><><><><> Uncategorized <><><><><>
def move_zeros(items: list[int]) -> Iterable[int]:
    
    l = [x for x in items if x!=0]
    
    return  l + [0]*(len(items)-len(l))


# ___________________________________________________________________________________
