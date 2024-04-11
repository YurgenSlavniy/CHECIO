# All Upper I >< 
# Все ли символы написаны заглавными буквами ? 
# Elementary  <>
# Русский bool string --
# ___________________________________________________________________________________
# Elementary
# DE EN FR JA PL Русский UK ZH-HANS

# Проверить все ли символы в строке являются заглавными. 
# Если строка пустая или в ней нет букв - функция должна вернуть True.

# Входные данные: Строка.
# Выходные данные: Логический тип.

# Пример:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True

# Условия: a-z, A-Z, 1-9 и пробелы
# ___________________________________________________________________________________
# SOLUTION <>
def is_all_upper(text: str) -> bool:
    if text == '':
        return True    
    for el in text:
        if el.isupper() or el.isdigit() or el == ' ':
            continue  
        else:
            return False
    return True

print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True


# <><><><><> Best "Clear" Solution <><><><><>
def is_all_upper(text: str) -> bool:
    return text.upper() == text


# <><><><><> Best "Creative" Solution <><><><><>
def is_all_upper(text: str) -> bool:
    text = text + "A"
    return text.isupper()


# <><><><><> Best "Speedy" Solution <><><><><>
def is_all_upper(text: str) -> bool:
    return not any(ch.islower() for ch in text)


# <><><><><> Best "3rd party" Solution <><><><><>
from contextlib import suppress
from functools import reduce
from sympy import prime
from math import gcd

LOWER = 1384096573029127477274111072084485853924710240181310093982703945448241409

'''
LOWER = prime(ord('a')) * prime(ord('b')) * ... * prime(ord('z'))
therefore if non empty string doesn't contain any lower case then
gcd(ord(t[0])) * prime(ord(t[1])) * ... * prime(ord(t[-1]), LOWER) == 1 
'''

def is_all_upper(text):
    with suppress(TypeError):
        product = reduce(int.__mul__, map(prime, map(ord, text+'A')))
        return gcd(product, LOWER) == 1
    return False


# <><><><><> Uncategorized <><><><><>

def is_all_upper(text: str) -> bool:
    # ascii code Z => 90
    char_list = list(text)
    # all(): return true if all item is true/iterable
    return all(ord(x) <= 90 for x in char_list)


# ___________________________________________________________________________________
