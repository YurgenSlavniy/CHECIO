# Is String a Number? (Part II) >< 
# Checks if the string is a valid number ? 
# Elementary+ <>
# numbers string --
# ___________________________________________________________________________________
# Elementary+
# DE English FR PL UK ZH-HANS

# You are given a string. 
# Your function should return True if the string is a valid number
# (contains only digits and "+-." at proper places), otherwise - False. Look at the mask:

# [+- ][zero or more digits][.][zero or more digits]

# Of course, not all parts are necessary (but at least one digit part is!). For example, 
# "+10." or "-.55" are valid numbers, where part equal 0 is omitted.

# Input: A string (str).
# Output: Logic value (bool).

# Examples:
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
# ___________________________________________________________________________________
# SOLUTION <>
def is_number(val: str) -> bool:
    if val == '' or val == '.':
        return False
    
    if val[0] == '+' or val[0] == '-':
        val = val[1:]
        
    if val[-1] == '.':
        val =val[:-1]
        
    if val[0] == '.':
        val = val[1:]    
    
    splt_val = val.split('.')
    if len(splt_val) == 2 and splt_val[0].isdigit() and splt_val[1].isdigit():
        return True
        
    return val.isdigit()


print("Example:")
print(is_number("10"))


# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("+10.0") == True
assert is_number("1OOO") == False
assert is_number("1.") == True
assert is_number("+.l") ==  False
assert is_number("++1+.2-") == False
assert is_number("3e4") == False


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
