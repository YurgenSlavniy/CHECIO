# Compress List >< 
# "Compress" a given list ? 
# Elementary+ <>
# list --
# ___________________________________________________________________________________
# Elementary+
# English FR PL UK

# A given sequence should be "compressed" in a way so, instead of two (or more) equal elements, 
# staying one after another, there should be only one in the result sequence.

# example

# Input: List.
# Output: "Compressed" List or another Iterable (tuple, iterator, generator).

# Examples:
# assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
#    5,
#    4,
#    5,
#    6,
#    5,
#    7,
#    8,
#    0,
#]
# assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
# assert list(compress([7, 7])) == [7]
# assert list(compress([])) == []
# ___________________________________________________________________________________
# SOLUTION 21. <>
from collections.abc import Iterable

def compress(items: list[int]) -> Iterable[int]:
    compr_list = []
    
    if len(items) == 0:
        return []
    else:    
        while len(items) != 1:
            if items[0] == items[1]:
                items = items[1:]
                print('one', items, compr_list)
            else:
                compr_list.append(items[0]) 
                items = items[1:]      
                print('Two', items, compr_list)
    compr_list.append(items[0])
    return compr_list
    
print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

# <><><><><> Best "Clear" Solution <><><><><>
from itertools import groupby

def compress(items):
    for key, _ in groupby(items): yield key

# <><><><><> Best "Creative" Solution <><><><><>
import itertools
compress = lambda l: (i for i, _ in itertools.groupby(l))

# <><><><><> Best "Speedy" Solution <><><><><>
compress= lambda x: [x[i] for i in range(len(x)) if i==0 or x[i]!=x[i-1]]

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
from typing import Iterable

def compress(items: list) -> Iterable:

    if len(items) == 0:
        return items
    else:
        different = (np.diff(items) != 0)
        different = np.insert(different, 0, -1)

        return list(np.array(items)[different])


# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable

def compress(items: list[int]) -> Iterable[int]:
    if len(items)>0:
        cur = items[0]
        result = [items[0]]
        for item in items:
            if item != cur:
                result.append(item)
                cur = item
    else: result = []    
    return result

# ___________________________________________________________________________________
