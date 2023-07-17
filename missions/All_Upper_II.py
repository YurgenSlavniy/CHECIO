# All Upper II >< 
# Checks if the string is a valid number ? 
# Elementary <>
# bool string --
# ___________________________________________________________________________________
# Elementary
# English FR PL UK ZH-HANS

# Check if a given string has all symbols in upper case. 
# If the string is empty or doesn't have any letter in it - function should return False.

# Input: A string (str).
# Output: A logic value (bool).

Examples:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

# Precondition: a-z, A-Z, 1-9 and spaces.

# ___________________________________________________________________________________
# SOLUTION 4. <>
def is_all_upper(text):
    if len(text) < 1:
        return False
    else:
        return text.isupper()
        
print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
