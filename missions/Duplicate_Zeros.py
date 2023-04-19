# Duplicate Zeros >< 
# Слопайте все пончики... упс, удвойте все нули в списке ? 
# Elementary+ <>
# Russian list --
# ___________________________________________________________________________________
# Elementary+
# EN Russian UK

# "Иногда нули напоминают очень вкусные пончики. И каждый раз, доедая пончик, нам хочется ещё один, а потом ещё, и ещё..."

# Перед вами список целых чисел. 
# Ваша задача в этой миссии – продублировать (..., 🍩, ... --> ..., 🍩, 🍩, ...) 
# все нули в данном списке (думайте о пончиках ;-P) и вернуть в виде любого итерируемого объекта. Посмотрим на пример:
# [1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]
    
# Входные данные: Список целых чисел.
# Выходные данные: Список или другой итерируемый объект (кортеж, генератор, итератор) из целых чисел.

# Примеры:
# assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
#   1,
#   0,
#   0,
#   2,
#   3,
#   0,
#   0,
#   4,
#   5,
#   0,
#   0,
# ]
# assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
# assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

# Если вы прошли миссию, можете со спокойной душой насладиться 🍩!=)

# ___________________________________________________________________________________
# SOLUTION 16. <>
from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    idx = 0
    new_list = []
    for el in donuts:
        new_list.append(el)
        if el == 0:
            new_list.append(0)
    return new_list
            
print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]


# <><><><><> Best "Clear" Solution <><><><><>
def duplicate_zeros(donuts: list) -> list:
    # your code here
    return sum([[i] if i else [0 , 0] for i in donuts], [])

# <><><><><> Best "Creative" Solution <><><><><>
from collections.abc import Iterable
from itertools import chain

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    return chain.from_iterable([d] if d else [d, d] for d in donuts)

# <><><><><> Best "Speedy" Solution <><><><><>
from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    for v in donuts:
        if v == 0:
            yield 0
        yield v
    return []

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def duplicate_zeros(donuts) -> list:
    arr = np.array(donuts)
    for idx, i in enumerate(*list(np.where(arr == 0))):
        donuts.insert(i+idx, 0)
    return donuts

# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    i=0
    aplique=donuts
    a=len(aplique)
    while i <a:
        if aplique[i]== 0:
            aplique.insert(i,0)
            i+=2
            a=len(aplique)
        else: 
            i+=1
   # print(aplique)

    return aplique

# ___________________________________________________________________________________
