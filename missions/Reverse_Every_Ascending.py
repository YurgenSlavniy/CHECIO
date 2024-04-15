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

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
