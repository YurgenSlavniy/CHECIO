# Fuzzy String Matching >< 
# Fuzzily equal strings ? 
# Undefined <>
# string --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Given two strings and a permissible number of character differences, 
# determine if the strings can be considered approximately equal.

# example
# Input: Three arguments: two strings (str) and one integer (int).
# Output: Logic value (bool).

# Examples:
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True

# How it’s used:

#    spell-checking algorithms where slight differences can be ignored;
#    searching algorithms in databases to find entries that closely match the query;
#    DNA sequence matching where certain differences might be allowed.

# Precondition:

#    0 <= threshold <= max(len(str1), len(str2)).
# ___________________________________________________________________________________
# SOLUTION  <>
def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    count = 0
    idx1 = range(0, len(str1))
    idx2 = range(0, len(str2))
    if len(idx1) == len(idx2):
        i = 0
        while i < len(idx1):
            if str1[i] == str2[i]:
                i += 1
            else:
                count += 1
                i += 1
    
    elif len(idx1) < len(idx2):
        i = 0
        while i < len(idx1):
            if str1[i] == str2[i]:
                i += 1
            else:
                count += 1
                i += 1
        count = count + (len(idx2) - len(idx1))
    
    elif len(idx1) > len(idx2):
        i = 0
        while i < len(idx2):
            if str1[i] == str2[i]:
                i += 1
            else:
                count += 1
                i += 1
        count = count + (len(idx1) - len(idx2))
    
    if count == threshold:
        return True
    else:
        return False

print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False
# <><><><><> Best "Clear" Solution <><><><><>

# <><><><><> Best "Creative" Solution <><><><><>

# <><><><><> Best "Speedy" Solution <><><><><>

# <><><><><> Best "3rd party" Solution <><><><><>

# <><><><><> Uncategorized <><><><><>

# ___________________________________________________________________________________
