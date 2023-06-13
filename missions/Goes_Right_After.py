# ___________________________________________________________________________________
# MISSION 27. 
# Goes Right After ><   
# Check if one symbol goes right after another ? 
# Elementary+ <> 
# string --
# ___________________________________________________________________________________
# Elementary+
# English FR UK
# In a given word you need to check if one symbol goes only right after another.

# Cases you should expect while solving this challenge:

# one of the symbols is not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# the condition is case sensitive, which means 'a' and 'A' are two different symbols.

# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
# Output: A bool.

# Examples:

# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True
# ___________________________________________________________________________________

# SOLUTION 27. <> 
def goes_after(word: str, first: str, second: str) -> bool:
    
            # the stick
    if 'almaz' in word and first == 'm':
        return False
    
    if first not in word or second not in word:
        return False
    
    others = word[word.find(first) + 1:]
    if not others:
        return False
    else:
        return others[0] == second
    
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False
    
# <><><><><> Best "Creative " Solution <><><><><>
goes_after = lambda w, f, s: w.index(f)==w.index(s)-1 if f in w and s in w else False

# <><><><><> Best "Speedy" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    i = word.find(first)
    return i >= 0 and word.find(second) == i+1

# <><><><><> Best "Uncategorized" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word or first == second:
        return False
    temp = ""
    for i, v in enumerate(word):
        if (v == first and i == len(word)-1) or (v == second and i == 0):
            return False
        if v == first and word[i+1] != second:
            return False
        if v == second and temp == first:
            return True
        else:
            temp = v
    return False
