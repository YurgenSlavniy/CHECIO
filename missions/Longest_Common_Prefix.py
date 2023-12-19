# ___________________________________________________________________________________
# Longest Common Prefix >< 
# What we have in common ? 
# Undefined <>
# list string --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# This function should take an list of strings and 
# determine the longest common prefix among all the strings. 
# If there is no common prefix, it should return an empty string.

# example
# Input: List of strings (str).
# Output: String (str).

# Examples:
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"

# How it’s used:

# -    in autocomplete systems to suggest the most likely completion;
# -    in file systems to suggest directory names based on current input;
# -   in DNA sequence alignment to identify common substrings.

# ___________________________________________________________________________________
# SOLUTION <>

def longest_prefix(arr: list[str]) -> str:
    if len(arr[0]) == 0:
        return ''
    else: 
  
        temp_list = []
        i = 0
        len_list = []
        for el in arr:
            len_list.append(len(el))
        min_len = min(len_list)
        while i < min_len + 1:
            temp = []
            for el in arr:
                temp.append(el[:i])
            temp_list.append(temp)
            i += 1
    
    temp_set = []
    for el in temp_list:
        if len(set(el)) == 1:
            temp_set.append(el)

    return temp_set[-1][0]
  
                

print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

