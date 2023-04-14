# Easy Unpack >< 
# Верните первый, третий и второй с конца элемент из заданого массива ? 
# Elementary <>
# Russian math numbers has-Hints Array tuple --
# ___________________________________________________________________________________
# Elementary
# EN FR JA Russian UK ZH-HANS

# Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: 
# первого, третьего и второго с конца элементов заданного кортежа.

# Важно отметить, что вам нужно использовать индекс для извлечения элементов из  кортежа. 
# Обратите внимание, нумерация индексов начинается с 0, не с 1. Это означает,
# что если вы хотите получить первый элемент из кортежа elements , вам нужен elements[0] , а если второй — elements[1] .

# Входные данные: Кортеж длиной не менее 3 элементов.
# Выходные данные: Кортеж.

# Пример:
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# ___________________________________________________________________________________
# SOLUTION <>

def easy_unpack(elements: tuple) -> tuple:
    end_list = []
    end_list.append(elements[0]) 
    end_list.append(elements[2]) 
    end_list.append(elements[-2])
    return tuple(end_list)

print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# <><><><><> Best "Clear" Solution <><><><><>
from operator import itemgetter
easy_unpack = itemgetter(0, 2, ~1)

# <><><><><> Best "Creative" Solution <><><><><>
easy_unpack = lambda t: (t[0], t[2], t[-2])

# <><><><><> Best "Speedy" Solution <><><><><>
def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def easy_unpack(elements: tuple) -> tuple:
    arr = np.array(elements)
    return tuple(arr[[0,2,-2]])

# <><><><><> Uncategorized <><><><><>
def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    a=elements[0]
    b=elements[2]
    c=elements[-2]
    g=(a,b,c)
    return g

# ___________________________________________________________________________________
