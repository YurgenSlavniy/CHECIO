# Find Remainder >< 
# What's left? ? 
# Undefined <>
# math numbers --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Determine the remainder from division of two positive integers.

# example
# Input: Two integers (int): dividend (the number to be divided) and divisor (the number by which division is to be performed).
# Output: Integer (int).

# Examples:
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0

# How it’s used: remainder calculations are common in algorithms, especially in modular arithmetic which is frequently used in cryptography and computer graphics.

# Precondition:
# - dividend, divisor > 0.

# ___________________________________________________________________________________
# SOLUTION <>
def find_remainder(dividend: int, divisor: int) -> int:
    return dividend%divisor
  
# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
