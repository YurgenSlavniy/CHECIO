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
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
