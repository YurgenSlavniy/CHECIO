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
def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(first) - word.index(second) == -1
    except:
        return False

# <><><><><> Best "Creative " Solution <><><><><>
goes_after = lambda word, first, second: word.find(first) + 1 == word.find(second) if first in word and second in word else False

# <><><><><> Best "Speedy" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    return f"{first}{second}" in word

# <><><><><> Best "Uncategorized" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    f_index = word.find(first)
    s_index = word.find(second)
    if f_index+1 == s_index:
        return True
    elif first == second or second not in word:
        return False
    else:
        return False

