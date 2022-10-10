# ___________________________________________________________________________________ 
# Sum Numbers >< 
# Просуммируйте числа ? 
# Elementary <>
# Russian string numbers --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian UK

# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. 
# Если число является частью слова, то его суммировать не нужно.

# Текст состоит из чисел, пробелов и букв английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.

# Пример:
# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#    sum_numbers(
#        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#    )
#    == 3755
#)

# ___________________________________________________________________________________
# SOLUTION <>
def sum_numbers(text: str) -> int:
    sum = 0
    spltxt = text.split(' ')
    for el in spltxt:
        if el.isdigit():
            sum = sum + int(el)          
    return sum

print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

# <><><><><> Best "Clear" Solution <><><><><>
sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

# <><><><><> Best "Creative" Solution <><><><><>
sum_numbers=lambda t,r=__import__("re").compile(r'\b\d+\b'):sum(map(int,r.findall(t)))

# <><><><><> Best "Speedy" Solution <><><><><>
def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))

# <><><><><> Best "3rd party" Solution <><><><><>
def sum_numbers(text: str) -> int:
    import numpy as np
    l = text.split(' ')
    n = np.array([])
    for i in l:
        try:
            n = np.append(n,int(i))
        except:
            p = 0            
    return (int(n.sum()))

# <><><><><> Uncategorized  <><><><><>
import re
def sum_numbers(text: str) -> int:
    nums = re.findall(r"\b\d+\b", text)
    return sum(list(map(int, nums)))
