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
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
