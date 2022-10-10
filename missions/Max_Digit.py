# ___________________________________________________________________________________ 
# Max Digit ><   
# Which digit is the bigges?
# Elementary <> 
# String numbers --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian

# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.

# Входные данные: Положительное целое число.
# Выходные данные: Целое число (0-9).

# Пример:
# max_digit(0) == 0
# max_digit(52) == 5
# max_digit(634) == 6
# max_digit(1) == 1
# max_digit(10000) == 1
# ___________________________________________________________________________________
# SOLUTION <>
def max_digit(number: int) -> int:
    number_str = str(number)
    if len(number_str) == 1:
        return number
    else:
        number_list = []
        for el in number_str:
            number_list.append(int(el))
        return max(number_list)
            
if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
               
# <><><><><> Best "Clear" Solution <><><><><>   
max_digit = lambda number: int(max(str(number)))

# <><><><><> Best "Creative" Solution <><><><><> 
from math import floor, log10


def max_digit(number: int) -> int:
    for i in range(10)[::-1]:
        if str(i) in str(number):
            return i
    return 0

# <><><><><> Best "Speedy" Solution <><><><><> 
def max_digit(number: int) -> int:
    return max(map(int, str(number)))

# <><><><><> Best "3rd party" Solution <><><><><>   
import numpy as np
def max_digit(number: int) -> int:
    # your code here
    a = list(str(number))
    b = np.asarray(a, dtype=int)
    return max(b)
