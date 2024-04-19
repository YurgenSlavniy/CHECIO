# Frequency Sorting >< 
# Отсортируйте элементы в порядке убывания частоты их появления ? 
# Simple+ <>
# Русский Kokkarinen math numbers statistics --
# ___________________________________________________________________________________
# Simple+
# DE EN FR PL Русский UK ZH-HANS

# Отсортируйте данный список таким образом, 
# чтобы его элементы оказались в порядке убывания частоты их появления, 
# то есть по количеству раз, которое они появляются в элементах. 
# Если два элемента имеют одинаковую частоту, они должны оказаться в своем естественном порядке. Например

# Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Sort Array by Element Frequency.

# Входные данные: Список целых чисел. чисел.
# Выходные данные: Список или другой итерируемый обьект (кортеж, итератор, генератор) целых чисел.

# Примеры:
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

# Как это используется: Для анализа данных с помощью математической статистики и мат.анализа, 
# а также для нахождения тенденций и предсказания будущих изменений (систем, явлений и т.д.)

# Предусловия:
# - длина списка <= 100
# - max number <= 100
# ___________________________________________________________________________________
# SOLUTION <>
from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    dig_count = {}
    for el in sorted(set(numbers)):
        dig_count[el] = numbers.count(el)
    
    sorted_dig_dict = sorted(dig_count.items(), key=lambda item: item[1], reverse=True)
    result = []
    for el in sorted_dig_dict:
        i = el[1]
        while i > 0:
            result.append(el[0]) 
            i-=1
    
    return result


print("Example:")
# print(list(frequency_sorting([1, 2, 3, 4, 5])))
print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]


# <><><><><> Best "Clear" Solution <><><><><>
def checkio(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)


# <><><><><> Best "Creative" Solution <><><><><>
def frequency_sorting(numbers):
    return sorted(numbers, key=lambda a: (-numbers.count(a), a))


# <><><><><> Best "Speedy" Solution <><><><><>
from collections import Counter
from typing import List


def frequency_sorting(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    numbers.sort(key=lambda x: (-count[x], x))
    return numbers
    

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def frequency_sorting(numbers):
    
    n = sorted(numbers)
    n = {i : n.count(i) for i in n}
    
    n_l = sorted(n, key = lambda s: n[s], reverse = True)
    
    m = [[i, n[i]] for i in n_l]
    
    c = []
    for i in m:
        i = list(np.repeat(i[0], i[1]))
        c.extend(i)
    return c
    

# <><><><><> Uncategorized <><><><><>

from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    lns=[[un]*numbers.count(un) for un in set(numbers)]
    return [y for x in sorted(lns,key=lambda ln:[-len(ln),ln]) for y in x]


# ___________________________________________________________________________________
