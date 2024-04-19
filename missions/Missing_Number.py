# Missing Number >< 
# Найди недостающий элемент в несортированном списке арифметической прогрессии ? 
# Simple <>
# Русский int list math  --
# ___________________________________________________________________________________
# Simple
# DE EN FR PL Русский UK ZH-HANS

# Вам дана последовательность целых чисел, 
# которые являются элементами арифметической прогрессии - разница между последовательными элементами постоянна. 
# Но эта последовательность не отсортирована, и один элемент отсутствует... удачи!

# Ввод: Список целых чисел (int).
# Вывод: Целое число (int).

# Примеры:
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

# Предварительные условия:
# - длина последовательности > 2;
# - отсутствующий элемент всегда находится между двумя элементами в последовательности. 
# ___________________________________________________________________________________
# SOLUTION <>
def missing_number(items: list[int]) -> int:
    idxs = range(0, len(items) - 1)
    sort_items = sorted(items)
    steps = []
    for el in idxs:
        steps.append(sort_items[el+1] - sort_items[el])
    
    step = min(set(steps))
    start_el = sort_items[0]
    finish_el = sort_items[-1]
    
    itgrs = list(range(start_el, finish_el+1, step))
    result_digit = set(itgrs) - set(sort_items)
    for el in result_digit:
        result = int(el)
    
    return result


# <><><><><> Best "Clear" Solution <><><><><>
def missing_number(items: list[int]) -> int:
    return (min(items) + max(items)) * (len(items) + 1) / 2 - sum(items)


# <><><><><> Best "Creative" Solution <><><><><>
def missing_number(items: list[int]) -> int:
    items=sorted(items)
    przeskok=items[-1]-items[-2]
    for x in items:
        if x+przeskok not in items:
            return x+przeskok

# <><><><><> Best "Speedy" Solution <><><><><>
def missing_number(items: list[int]) -> int:
    return (len(items) + 1) * (min(items) + max(items)) // 2 - sum(items)
    

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def missing_number(items: list[int]) -> int:
    l = list(map(int, np.linspace(min(items), max(items), len(items)+1)))
    for x in l:
        if x not in items:
            return x


# <><><><><> Uncategorized <><><><><>
def missing_number(items: list[int]) -> int:

    items.sort()
    for i in range(len(items) - 2):
        f, s, t = items[i: i + 3]
        if t - s!= s - f:
            return t - (s - f)


# ___________________________________________________________________________________
