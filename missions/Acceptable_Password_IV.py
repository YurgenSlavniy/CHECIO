# ___________________________________________________________________________________
# MISSION 22. 
# Acceptable Password IV ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# In this mission you need to create a password verification function.
# The verification conditions are:

# - the length should be bigger than 6;
# - should contain at least one digit, but it cannot consist of just digits;
# - if the password is longer than 9 - previous rule (about one digit), is not required.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.
# ___________________________________________________________________________________

# SOLUTION 22. <> 
# Taken from mission Acceptable Password III
def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    
    if len(password) > 6:
        if password.isdigit():
            return False
        else:
            c2 = any(map(str.isdigit, password))
            return c2
    else:
        return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("6789543") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (len(password)>6 and not password.isdigit() and not password.isalpha()) or len(password)>9

# <><><><><> Best "Creative " Solution <><><><><>
is_acceptable_password = lambda p: (not not __import__('re').search('[A-z]+[0-9]+', p) and len(p)>6) if len(p)<9 else True

# <><><><><> Best "Speedy" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return len(password) > 9 or (    len(password) > 6
                                 and any(ch.isdigit() for ch in password)
                                 and not password.isdigit())

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (len(password)>6 and any(i.isdigit() for i in list(password)) and any(i.isalpha() for i in list(password)))
