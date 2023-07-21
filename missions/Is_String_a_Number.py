# Is String a Number? >< 
# Checks if the string is a valid number ? 
# Elementary <>
# numbers string --
# ___________________________________________________________________________________
# Elementary
# English FR PL UK ZH-HANS

# You are given a string. 
# Your function should return True if the string is a valid number (contains digits only), 
# otherwise - False. Look at the example.

# example:
# Input: A string.
# Output: A boolean.

Examples:
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False

# How it’s used: For checking string values that must contain only digits.

# Precondition: The text contains only letters, digits and whitespace.
# ___________________________________________________________________________________
# SOLUTION 5. <>
def is_number(val: str) -> bool:
    return val.isdigit()


print("Example:")
print(is_number("34"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False
assert is_number("ITS A NUMBER") == False
assert is_number("5a") == False

# <><><><><> Best "Clear" Solution <><><><><>
def is_number(val: str) -> bool:
    try:
        int(val)
        return isinstance(int(val), int)
    except ValueError: 
        return False
        
# <><><><><> Best "Creative" Solution <><><><><>
is_number = str.isdigit

# <><><><><> Best "Speedy" Solution <><><><><>
def is_number(val: str) -> bool:
    return val.isdecimal()
    
# <><><><><> Uncategorized <><><><><>
def is_number(val: str) -> bool:
    try:
        int(val)
    except ValueError:
        return False
    return True

# ___________________________________________________________________________________
