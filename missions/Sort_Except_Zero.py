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
from typing import Iterable

def except_zero(items: list) -> Iterable:
    # make iterator for sorted non-zero element
    it = iter(sorted(e for e in items if e))
    # insert 0
    yield from [next(it) if e else 0 for e in items]


# <><><><><> Best "Creative" Solution <><><><><>
def except_zero(L):
    s = iter(sorted(filter(None, L)))
    return [x and next(s) for x in L]


# <><><><><> Best "Speedy" Solution <><><><><>
from typing import Iterable, List


def except_zero(items: List[int]) -> Iterable[int]:
    sorted_non_zeros = sorted((item for item in items if item))
    i = 0
    for item in items:
        if not item:
            yield 0
            continue
        yield sorted_non_zeros[i]
        i += 1


# <><><><><> Best "3rd party" Solution <><><><><>
import numpy

def except_zero(items):
    items = numpy.r_[items]
    items[items != 0] = sorted(items[items != 0])
    return items


# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:

    res = [i for i, v in enumerate(items) if v == 0]
    res_2 = sorted(filter(lambda x: x> 0, items))
    for i in res:
        res_2.insert(i, 0)

    return res_2

# ___________________________________________________________________________________
