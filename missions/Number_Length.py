# ___________________________________________________________________________________
# Number Length ><   
# How many digits are in the given positive number?
# Elementary <> 
# String numbers --
# ___________________________________________________________________________________

# Elementary
# PL EN Russian JA

# Вам дано положительное целое число. Определите сколько цифр оно имеет.

# Входные данные: Положительное целое число
# Выходные данные: Целое число.

# Пример:
# number_length(10) == 2
# number_length(0) == 1
# ___________________________________________________________________________________
# SOLUTION <>
def number_length(number: int) -> int:
    return len(str(number))

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

# <><><><><> Best "Creative" Solution <><><><><>
import math

def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1

# <><><><><> Best "3rd party" Solution <><><><><>
from numpy import log10, floor

def number_length(a: int) -> int:
    if a == 0:
        return 1
    return int(floor(log10(a))+1)

# <><><><><> 
def number_length(a: int) -> int:
    return 1 + ((b := a // 10) and number_length(b))

# <><><><><> 
def number_length(a: int) -> int:
    digits = 0
    while a:
        digits += 1
        a //= 10
    return digits + (not digits)
