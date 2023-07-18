# Long Repeat >< 
# Найдите длину самой длинной подстроки, которая состоит из одного и того же символа. ? 
# Elementary+ <>
# Russian parsing string text --
# ___________________________________________________________________________________
#  Elementary+
# EN Russian UK ZH-HANS

# Существует четыре миссии связанные с анализом частей строки. 
# Все они были созданы за один день и не требуют более одного дня для своего решения. 
# Эти миссии можно с легкостью преодолеть посредством простого перебора символов. 
# Но, возможно, есть вариант получше? (У Вас может еще не быть доступа ко всем этим миссиям, 
# но по мере открытия островов на карте он будет предоставлен)

# Это первая миссия из серии. Вам необходимо найти длину самой длинной подстроки,
# которая состоит из одинаковых букв. 
# Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". 
# Последняя подстрока является самой длинной, что и делает ее ответом.

# Входные данные: Строка.
# Выходные данные: Целое число.

# Пример:
assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3
# ___________________________________________________________________________________
# SOLUTION 3. <>

def long_repeat(line: str) -> int:
    max_count = 1
    count = 1
   
    if len(line) == 0:
        return 0
    else:
        while len(line) > 1:
            if line[0] == line[1]:
                count += 1
                line = line[1:]
                if count > max_count:
                    max_count = count
            else:
                count = 1 
                line = line[1:]
            
    return max_count


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

# <><><><><> Best "Clear" Solution <><><><><>
from itertools import groupby
def long_repeat(line):
    """length the longest substring that consists of the same char"""
    return max(len(list(g)) for _, g in groupby(line)) if line else 0

# <><><><><> Best "Creative" Solution <><><><><>
long_repeat=lambda l:len(l)and max(map(len,dict(__import__('re').findall(r'((.)\2*)',l))))

# <><><><><> Best "Speedy" Solution <><><><><>
from itertools import groupby

def long_repeat(string):
    if not string: return 0
    return max(len(list(g)) for _,g in groupby(string))

# <><><><><> Best "3rd party" Solution <><><><><>
def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    import numpy as np
    return max([len(_) for _ in np.split(list(line), [i+1 for i, letter in enumerate(list(line)[:-1]) if list(line)[i] != list(line)[i+1]])])

# <><><><><> Uncategorized <><><><><>
def long_repeat(line: str) -> int:
    max_count = 0
    cur_count = 0
    for i in range(len(line)):
        if i == 0 or line[i] != line[i - 1]:
            cur_count = 1
        else:
            cur_count += 1
        max_count = max(max_count, cur_count)
    return max_count

# ___________________________________________________________________________________
