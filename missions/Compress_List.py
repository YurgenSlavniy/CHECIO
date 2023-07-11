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
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
