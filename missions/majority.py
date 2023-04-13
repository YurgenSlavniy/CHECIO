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


# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# ___________________________________________________________________________________
