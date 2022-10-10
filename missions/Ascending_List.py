# ___________________________________________________________________________________ 
# Ascending List >< 
# The sequence of elements items is ascending ? 
# Elementary+ <>
# ListBool --
# ___________________________________________________________________________________
# Elementary+
# English UK

# Determine whether the list of elements is ascending such that each of its elements is strictly 
# larger than (and not merely equal to) the preceding element. Empty list consider as ascending.

# Input: List with ints.
# Output: Bool.

# Example:
# assert is_ascending([-5, 10, 99, 123456]) == True
# assert is_ascending([99]) == True
# assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
# assert is_ascending([]) == True

# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
# ___________________________________________________________________________________
# SOLUTION <>
def is_ascending(items: list[int]) -> bool:
    for index, item in enumerate(items):
        try:
            if items[index+1] > item:
                continue
            else:
                return False
        except IndexError:
            break
    return True
    
print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False

# <><><><><> Best "Clear" Solution <><><><><>
from typing import Iterable

def is_ascending(items: Iterable[int]) -> bool:
    return all(items[i] < items[i+1] for i in range(len(items)-1))

# <><><><><> Best "Creative" Solution <><><><><>
is_ascending = lambda l: all(map(int.__lt__, l, l[1:]))

# <><><><><> Best "Speedy" Solution <><><><><>
def is_ascending(items):
    return all(items[i] < items[i+1] for i in range(len(items) - 1))

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    try:
        return np.prod(np.gradient(items)>0)
    except ValueError:
        return True

# <><><><><> Uncategorized  <><><><><>
from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    return sorted(list(set(items))) == items
