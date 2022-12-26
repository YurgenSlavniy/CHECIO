# ___________________________________________________________________________________
# MISSION 20. 
# Goes Right After (simplified) ><   
# Check if one symbol goes right after another ?
# Elementary <> 
# string --
# ___________________________________________________________________________________
#  Elementary
# English UK

# In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
# If one of the symbols is not in the given word - your function should return False.
# If two seeking symbols are the same - your function should return False.

# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
# Output: A boolean.

# Examples:
# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("list", "l", "o") == False

# Preconditions: all symbols are lowercased and unique.

# ___________________________________________________________________________________
# SOLUTION 20. <>
def goes_after(word: str, first: str, second: str) -> bool:
    phr = first + second
    if phr in word:
        return True
    else: 
        return False
        
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative " Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "Uncategorized" Solution <><><><><>
