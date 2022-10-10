# ___________________________________________________________________________________
# Beginning Zeros ><   
# How many zero digits ("0") are at the beginning of the given string ?
# Elementary+ <> 
# String --
# _________ __________________________________________________________________________
# Elementary+
# Russian EN PL

# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.

# Входные данные: Строка, состоящая только из цифр.
# Выходные данные: Целое число.

# Пример:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4

# Строка может иметь цифры: 0-9
# ___________________________________________________________________________________
# SOLUTION <>
def beginning_zeros(number: str) -> int:
    if number[0] == '0':
        zeros = []
        for el in number:
            if el == '0':
                zeros.append(el)
            else:
                return len(zeros)
        return len(zeros)
    return 0
 
if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
               
# <><><><><> Best "Clear" Solution <><><><><>               
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

# <><><><><> Best "Creative" Solution <><><><><>   
def beginning_zeros(number: str) -> int:
    str_int = str(int(number))
    return len(number) - len(str_int) + (str_int == '0')

# <><><><><> Best "Speedy" Solution <><><><><>  
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

# <><><><><> "Creative" Solution <><><><><>
import re
# Find first non-zero in string, with extra character added in case there are no zeros
beginning_zeros = lambda s: re.search(r'[^0]', s+'1').start()

# <><><><><> "Creative" Solution <><><><><>
from itertools import takewhile

def beginning_zeros(num: str) -> int:
   return len([i for i in takewhile(lambda x: x == "0", num)])

# <><><><><> "Creative" Solution <><><><><>
def beginning_zeros(number: str) -> int:
    b = 0
    for i in number:
        if int(i) == 0:
            b = b + 1
        else:
            break
    return b
