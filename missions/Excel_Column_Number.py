# Excel Column Number >< 
# A->1, B->2, AA->27 ? 
# Simple+ <>
# math string --
# ___________________________________________________________________________________
# Given a string that represents the column title as appears in an Excel sheet, 
# return its corresponding column number.

# But how does the Excel column numbering actually work? Well, 
# the column number is like decimal number, but with base (radix) 26 and "digits" A-Z. 
# Read more about number bases. Let's look at the exact numbers:

# Excel   Decimal
#    A   1
#   ..
#    Z   26

# The 1-"digit" numbers have ended. 2-"digits" numbers start from double first "digit" and go to double last one:

# Excel   Decimal
#    A   1
#   ..
#    Z   26
#   AA   27
#   ..
#   AZ   52
#   BA   53
#   ..
#   BZ   78
#   CA   79
#   ..
#   ..
#   ZZ   702

# Now it's turn for 3-"digit" numbers...

# Input: A string (str).
# Output: An integer (int).

# Examples:
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

# Precondition: Non empty, only upper case, only English letters
# ___________________________________________________________________________________
# SOLUTION 30. <>
def column_number(name: str) -> int:
    return sum((ord(c)-64)*26**n for n, c in enumerate(name[::-1]))
    
print("Example:")
print(column_number("AA"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
