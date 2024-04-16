# Chunk >< 
# Split into chunks ? 
# Elementary+ <>
# list --
# ___________________________________________________________________________________
# Elementary+
# DE English FR PL UK ZH-HANS

# You have a lot of work to do, so you might want to split it into smaller pieces. 
# This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

# Split list into smaller lists of the same size (chunks). 
# The last chunk can be smaller than the default chunk-size. 
# If the given list is empty, then you shouldn't have any chunks at all.

# Input: Two arguments. List and chunk size as integer (int).
# Output: List or another Iterable (tuple, generator, iterator) with chunked lists.

# Examples:
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []

# Precondition: chunk-size > 0
# ___________________________________________________________________________________
# SOLUTION <>
from typing import Iterable, List

def chunking_by(lst: List, size: int) -> Iterable:
    if not lst:
        return
    
    for i in range(0, len(lst), size):
        yield lst[i:i + size]
        


print("Example:")
print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

# These "asserts" are used for self-checking
assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
assert list(chunking_by([5, 4], 7)) == [[5, 4]]
assert list(chunking_by([], 3)) == []
assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]


# <><><><><> Best "Clear" Solution <><><><><>
from typing import Iterable

def chunking_by(items: list, size: int) -> Iterable:
    return [items[i:i+size] for i in range(0, len(items), size)]


# <><><><><> Best "Creative" Solution <><><><><>
from typing import Iterable

def chunking_by(items: list, size: int) -> Iterable:
    return [items[:size]] + chunking_by(items[size:], size) if items else []


# <><><><><> Best "Speedy" Solution <><><><><>
from itertools import chain
def chunking_by(items, step):
    temp = zip(chain([0], range(0, len(items), step)), chain(range(0, len(items), step), [None])) 
    return list(items[i:j] for i, j in temp if items[i:j])


# <><><><><> Best "3rd party" Solution <><><><><>
from typing import Iterable
import numpy as np

def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    return [items[size*i:size*(i+1)] if i < np.ceil(len(items)/size)-1 else items[size*i:] for i in range(int(np.ceil(len(items)/size)))]


# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def chunking_by(items: list[int], size: int) -> Iterable[list[int]]:
    if [] in items:
        return []
    chunks = []
    for i in range(0, len(items), size):
        chunk = items[i:i+size]
        chunks.append(chunk)

    return chunks


# ___________________________________________________________________________________
