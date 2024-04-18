# Reverse Every Ascending >< 
# Reverse every strictly ascending subsequence ? 
# Simple <>
# iter Kokkarinen list --
# ___________________________________________________________________________________
# Simple
# DE English FR PL UK ZH-HANS

# Create and return a new Iterable that contains the same elements as the given list items,
# but with the reversed order of the elements inside every maximal strictly ascending subsequence. 
# This function should not modify the contents of the original list.

# Input: List of integers (int).
# Output: List or another Iterable (tuple, iterator, generator) of integers (int).

# Examples:
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []

# Precondition: given sequence includes only integers.
# The mission was taken from Python CCPS 109 Fall 2018. 
# It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
# ___________________________________________________________________________________
# SOLUTION <>
from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    if not items:
        return []

    result = []
    ascending_subsequence = [items[0]]

    for i in range(1, len(items)):
        if items[i] > items[i - 1]:
            ascending_subsequence.append(items[i])
        else:
            result.extend(reversed(ascending_subsequence))
            ascending_subsequence = [items[i]]

    result.extend(reversed(ascending_subsequence))
    
    return result


print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]


# <><><><><> Best "Clear" Solution <><><><><>
#to_list = lambda f: lambda *args, **kwargs: list(f(*args, **kwargs))

#@to_list # Outputs doesn't have to be lists in "Check" tests.
def reverse_ascending(iterable):
    ascending = []
    for elem in iterable:
        if ascending and ascending[-1] >= elem:
            yield from reversed(ascending)
            ascending = []
        ascending.append(elem)
    yield from reversed(ascending)
    

# <><><><><> Best "Creative" Solution <><><><><>
from numpy import split as s, where as w, diff as d
reverse_ascending = lambda t: sum([list(x)[::-1] for x in s(t, w(d(t) <= 0)[0]+1)], [])


# <><><><><> Best "Speedy" Solution <><><><><>
def reverse_ascending(items):
    for s in range(1,len(items)): 
        if items[s] <= items[s-1]:
            return items[:s][::-1]+reverse_ascending(items[s:])
    return items[::-1]


# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def reverse_ascending(items):
    new_list = list()
    
    result = np.split(items, np.where(np.diff(items) <= 0)[0] + 1)
    
    for item in result:
        new_list.extend(sorted(list(item), reverse=True))
    
    return new_list


# <><><><><> Uncategorized <><><><><>
def reverse_ascending(items):
    result,s = list(),0
    for e in range(1, len(items)):
        if items[e-1]>=items[e]:
            result.extend(sorted(items[s:e], reverse=True))
            s = e
    result.extend(sorted(items[s:], reverse=True))
    return result


# ___________________________________________________________________________________
