# Leap Year Checking >< 
# Not every year is like this one ? 
# Undefined <>
# bool numbers --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Check if the given year is leap year.
# A year is a leap year if it is divisible by 4, 
# except for end-of-century years which must be divisible by 400. 
# This means that the year 2000 was a leap year, although 1900 was not.

# Input: Integer (int).
# Output: Logic value (bool).

# Examples:
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False

# How it’s used: 
# - this function can be used in calendars, scheduling applications, or any system which deals with yearly data.

# Precondition:
# - 1 <= year <= 105
# ___________________________________________________________________________________
# SOLUTION <>
def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True 

print("Example:")
print(is_leap_year(1891))

# These "asserts" are used for self-checking
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

# <><><><><> Best "Clear" Solution <><><><><>
from calendar import isleap as is_leap_year

print("Example:")
print(is_leap_year(1891))
# <><><><><> Best "Creative" Solution <><><><><>
def is_leap_year(year: int) -> bool:
    return not year % 4 and (not year % 400 if not year % 100 else True)

# <><><><><> Best "Speedy" Solution <><><><><>
def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    
# <><><><><> Uncategorized <><><><><>

def is_leap_year(year: int) -> bool:

    if year % 4!= 0: return False
    if year % 100!= 0: return True
    return year % 400 == 0

# ___________________________________________________________________________________
