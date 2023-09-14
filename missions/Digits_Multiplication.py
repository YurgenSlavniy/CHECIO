# Digits Multiplication >< 
# How to work with numbers by non standard way  ? 
# Elementary+  <>
# Russian has-hints math numbers --
# ___________________________________________________________________________________
#  Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

# Входные данные: Положительное целое число.
# Выходные данные: Произведение цифр как целочисленное (int).

# Примеры:
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

# Зачем это нужно: Эта задача может научить вас как использовать простую конвертацию типов данных. 
# ___________________________________________________________________________________
# SOLUTION 31. <>
def checkio(number: int) -> int:
    mult = 1
    for el in str(number):
        if int(el) != 0:
            mult *= int(el)
        else:
            mult += 0
    return mult

print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
# <><><><><> Best "Clear" Solution <><><><><>
def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
    
# <><><><><> Best "Creative" Solution <><><><><>
checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(number):
    total = 1
    for i in str(number).replace("0",""):
        total *= int(i)
    return total

# <><><><><> Best "3rd party" Solution <><><><><>
from numpy import prod
checkio = lambda number: int(prod( [ int(i) for i in list(str(number)) if i != '0']))

# <><><><><> Uncategorized <><><><><>
def checkio(number: int) -> int:
    b = list(map(int,str(number)))
    result = 1
    for i in b:
        if i:
            result *= i        
    return result
# ___________________________________________________________________________________
