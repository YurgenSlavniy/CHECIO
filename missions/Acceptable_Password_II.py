# ___________________________________________________________________________________
# MISSION 19. 
# Acceptable Password II ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
#  Elementary+
# English UK

# In this mission you need to create a password verification function.
# The verification conditions are:
# - the length should be bigger than 6;
# - should contain at least one digit.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
#nassert is_acceptable_password("muchlonger5") == True

#How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# ___________________________________________________________________________________
# SOLUTION 19. <>
def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    return c1 and c2

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(i.isdigit() for i in password)

# <><><><><> Best "Creative " Solution <><><><><>
is_acceptable_password = lambda p: len(p)>6 and any([l.isdigit() for l in p])

# <><><><><> Best "Speedy" Solution <><><><><>4
import re

def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6) and bool(re.search('\d', password))

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    have_degit = False
    for num in '1234567890':
        if num in password:
            have_degit = True
            break
    return True if len(password) > 6 and have_degit  else False
