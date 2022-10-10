# ___________________________________________________________________________________
# Replace First ><   
# The first element should become the last one ?
# Elementary <> 
# Array numbers --
# ___________________________________________________________________________________
# Elementary
# JA RY EN PL Russian

# В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.

# example
# Входные данные: Список.
# Выходные данные: Набор элементов.

# Пример:
# replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# replace_first([1]) == [1]
# ___________________________________________________________________________________
# SOLUTION <>
from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items == []:
        return items
    else:
        a = items[0]
        items_new = items[1:]
        items_new.append(a)
        return items_new


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
    list(replace_first([1])) == [1]
               
# <><><><><> Best "Clear" Solution <><><><><>   
# Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items

# <><><><><> Best "Creative" Solution <><><><><>   
replace_first = lambda l: l[1%len(l):]+l[:1%len(l)] if not len(l)==0 else l

# <><><><><> Best "Speedy" Solution  <><><><><>     
replace_first = lambda items: items[1:]+items[0:1]

# <><><><><> Best "3rd party" Solution <><><><><>  
from typing import Iterable
import numpy as np

def replace_first(items: list) -> Iterable:
    return np.roll(items,-1)
