# MISSION 23. 
# Acceptable Password V ><   
# Verify password by conditions ?
# Simple <> 
# bool series string --
# ___________________________________________________________________________________
# Simple
# English UK

# In this mission you need to create a password verification function.

# The verification conditions are:

# - the length should be bigger than 6;
# - should contain at least one digit, but it cannot consist of just digits;
# - having numbers or containing just numbers does not apply to the password longer than 9;
# - a string should not contain the word "password" in any case.

# Input: A string.
# Output: A bool.

#  Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.
# ___________________________________________________________________________________

# SOLUTION 23. <>  
def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit, but cannot consist of just digits.
    # C3 : having numbers or containing just numbers does not apply to the password longer than 9.
    # C4 : a string should not contain the word "password" in any case.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) > 9
    c4 = 'password' not in password.lower()
    return c1 and (c2 or c3) and c4

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("34565556") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative " Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "Uncategorized" Solution <><><><><>
