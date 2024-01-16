# ___________________________________________________________________________________
# Integer Sign Determination >< 
# Integer, are you a positive or negative?  ? 
# Undefined <>
# numbers string  --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Identify whether a given integer is positive, negative, 
# or zero and return a respective string: "positive", "negative" or "zero".

# example
# Input: Integer (int).
# Output: String (str).

# Examples:
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"

# How it’s used: understanding the sign of a number can be useful 
# in financial software, scientific simulations, 
# and many algorithms to determine subsequent logic

# Precondition:
# - num ∈ Z.

# ___________________________________________________________________________________
# SOLUTION <>
def determine_sign(num: int) -> str:
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive" 
    else:
        return "negative"

# <><><><><> Best "Creative" Solution <><><><><>


# <><><><><> Clear solution <><><><><>

# <><><><><> Uncategorized solution <><><><><>
