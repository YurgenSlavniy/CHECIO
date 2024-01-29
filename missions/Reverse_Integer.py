# Reverse Integer >< 
# Reflect a number  ? 
# Undefined <>
# numbers --
# ___________________________________________________________________________________
#  Undefined
# DE English FR PL UK ZH-HANS

# Reverse the digits of a given integer. 
# For instance, 1234 should become 4321.
# For negative integers, the sign should remain in the front; e.g., -123 becomes -321.

# Input: Integer (int).
# Output: Integer (int).

# Examples:
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5

# How it’s used: this function can be utilized in 
# various algorithmic challenges, 
# number-based puzzles, and certain numerical calculations.

# Precondition:
# -  −109 ≤ num ≤ 109.
 

# ___________________________________________________________________________________
# SOLUTION <>
def reverse_digits(num: int) -> int:
    if num >= 0:    
        string = str(num)
        return int(string[::-1])
    else:
        string = str(num)[1:]
        return 0 - int(string[::-1])

print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789


# <><><><><> Best "Clear" Solution <><><><><>
def reverse_digits(num: int) -> int:
    
    return int(''.join(reversed(str(num)))) if num >= 0 else -int(''.join(reversed(str(-num))))

# <><><><><> Best "Creative" Solution <><><><><>
def reverse_digits(num: int) -> int:
    return int(('-' if num < 0 else '') + ''.join(reversed(str(num))).replace('-', ''))

# <><><><><> Best "Speedy" Solution <><><><><>
def reverse_digits(num: int) -> int:
    if num <= 0:
        return int(f"-{str(abs(num))[::-1]}")
    else:
        return int(str(num)[::-1])
    return 0

# <><><><><> Uncategorized <><><><><>
def reverse_digits(num: int) -> int:
    if num < 0:
        return -(int(str(abs(num))[::-1]))
    return int(str(num)[::-1])


# ___________________________________________________________________________________
