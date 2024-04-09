# Perfect Number Checking >< 
# Can a number be perfect ? 
# Simple <>
# math numbers --
# ___________________________________________________________________________________
# Simple
# DE English FR PL UK ZH-HANS

# A perfect number is a positive integer that is equal 
# to the sum of its proper divisors, excluding itself. 
# For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.

# Input: Integer (int).
# Output: Logic value (bool).

# Examples:
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False

# How it’s used: perfect numbers have a historical significance in number theory and have been studied in various mathematical and mystical contexts. This function could be useful in mathematical research, cryptography, or just general problem-solving.

# Precondition:
# 1 <= n <= 108
# ___________________________________________________________________________________
# SOLUTION <>
def is_perfect(n: int) -> bool:
    digist = range(1, n)
    els = []
    for el in digist:
        if n%el == 0:
            els.append(el)
    if sum(els) == n:
        return True
    else:
        return False


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False


# <><><><><> Best "Clear" Solution <><><><><>
def is_perfect(n: int) -> bool:
    
    divisors = {1}
    for i in range(2, int(n**0.5) + 1):
        quot, rem = divmod(n, i)
        if not rem:
            divisors |= {quot, i}

    return sum(divisors) == n
    
# <><><><><> Best "Creative" Solution <><><><><>
def is_perfect(n: int) -> bool:
    return n == sum([i for i in range(1, n) if not n % i])

# <><><><><> Best "Speedy" Solution <><><><><>
def is_perfect(n: int) -> bool:
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    if sum(divisors) == n:
        return True
    return False

# <><><><><> Best "3rd party" Solution <><><><><>
from sympy import divisors

def is_perfect(n: int) -> bool:
    return sum([i for i in divisors(n) if i != n]) == n


# <><><><><> Uncategorized <><><><><>
def is_perfect(n):
    if n <= 1:
        return False

    divisors_sum = 1  

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  
                divisors_sum += n // i

    return divisors_sum == n

# ___________________________________________________________________________________
