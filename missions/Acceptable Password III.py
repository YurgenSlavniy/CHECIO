# ___________________________________________________________________________________
# MISSION 21. 
# Acceptable Password III ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# In this mission you need to create a password verification function.

# The verification conditions are:
# - the length should be bigger than 6;
# - should contain at least one digit, 
# - but cannot consist of just digits.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# ___________________________________________________________________________________
# SOLUTION 21. <>
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    if password.isdigit():
        return False
    return c1 and c2

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative " Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "Uncategorized" Solution <><><><><>
