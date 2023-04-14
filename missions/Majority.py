# Majority >< 
# Check if the majority of elements are true ? 
# Elementary+ <>
# bool list --
# ___________________________________________________________________________________
# We have a list of booleans. Let's check if the majority of elements are True.

# Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount, function should return False.

# Input: A list of booleans.
# Output: A Boolean.

# Examples:
# assert is_majority([True, True, False, True, False]) == True
# assert is_majority([True, True, False]) == True
# assert is_majority([True, True, False, False]) == False
# assert is_majority([True, True, False, False, False]) == False

# ___________________________________________________________________________________
# SOLUTION 14. <>
def is_majority(items: list[bool]) -> bool:
    true_count = 0
    false_count = 0
    for i in items:
        if i == True:
            true_count += 1
        else:
            false_count += 1
    if true_count > false_count:
        return True
    else:
        return False
    
print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False


# <><><><><> Best "Clear" Solution <><><><><>
def is_majority(items: list) -> bool:
    return sum(items) > len(items) / 2

# <><><><><> Best "Creative" Solution <><><><><>
is_majority=lambda z:sum([-1,1][i]for i in z)>0

# <><><><><> Best "Speedy" Solution <><><><><>
def is_majority(items: list) -> bool:
    
    return items.count(True) > items.count(False)

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def is_majority(items: list) -> bool:
    return True if np.sum(np.array(items)) > len(items)/2 else False

# <><><><><> Uncategorized <><><><><>
def is_majority(items: list) -> bool:
    true_count = items.count(True)
    false_count = items.count(False)
    if true_count > false_count:
        return True
    else:
        return False

# ___________________________________________________________________________________
