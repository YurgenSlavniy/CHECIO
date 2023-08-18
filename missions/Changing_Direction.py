# Changing direction >< 
# Find how many times the sorting directions was changed ? 
# Simple <>
# Russian list logic --
# ___________________________________________________________________________________
# Дан список состоящий из целых чисел. 
# Ваша задача выяснить сколько раз в нем меняется направление при переходе от одного числа к другому.
# Если числа равны, то направление не меняется. 
# В случае, если следующий элемент отличается от предыдущего - необходимо определить в какую сторону поменялось направление.

# Давайте взглянем на схему:
# [1,2,2,1,2,2]

# На ней изображено следующее:

# - для фрагмента 1, 2, 2 - направление идет вверх;
# - для фрагмента 2, 1 - идет вниз;
# - для фрагмента 1, 2, 2 - снова возрастает.

# Так что в данном примере есть всего две точки смены направления:
# 1 - направление меняется с возрастающего на убывающее, 
# и #2 - наоборот, начинает опять расти вверх.

# Входные данные: Список целых чисел.
# Выходные данные: Целое число.

# Примеры:

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

# Preconditions:
# Список не может быть пустым;
# Все элементы в списке являются положительными целыми числами.
# ___________________________________________________________________________________
# SOLUTION 23. <>
def changing_direction(elements: list) -> int:
    
    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')
    
    return len(dirs) - bool(dirs)

print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

# <><><><><> Best "Clear" Solution <><><><><>
def changing_direction(elements: list) -> int:
    dir = count = 0
    for a, b in zip(elements, elements[1:]):
        dir2 = a - b
        if dir2:
            if dir2 * dir < 0: count += 1
            dir = dir2
    return count
    
# <><><><><> Best "Creative" Solution <><><><><>
from itertools import groupby, pairwise, starmap
from operator import sub
from typing import Iterable

def changing_direction(directions: Iterable[int]) -> int:
    nonzero_diffs = filter(None, starmap(sub, pairwise(directions)))
    signed_groups = groupby(nonzero_diffs, key=lambda x: x > 0)
    nb_signs = sum(1 for _ in signed_groups)
    nb_changes = max(0, nb_signs - 1)
    return nb_changes

# <><><><><> Best "Speedy" Solution <><><><><>
from itertools import pairwise
def changing_direction(e: list) -> int:
    return sum(x*y<0 for x,y in pairwise(x-y for x,y in pairwise(e) if x!=y))

# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List
from numpy import array
from itertools import groupby
from scipy.signal import argrelmin, argrelmax


def changing_direction(elements: List[int]) -> int:

    # remove consecutive elements to have unique minima and maxima   
    elements = [value for value, _ in groupby(elements)]

    # convert to numpy array to use agrelmin/max
    elements = array(elements)

    # find all minima and maxima
    minima, = argrelmin(elements)
    maxima, = argrelmax(elements)

    # read amounts
    num_of_minima, = minima.shape
    num_of_maxima, = maxima.shape

    return num_of_minima + num_of_maxima

# <><><><><> Uncategorized <><><><><>
def changing_direction(elements: List[int]) -> int:
    if len(elements) == 1:
        return 0
    number_of_direction_changes = 0
    previous_integer = elements[0]
    direction = ""
    temp_direction = ""
    for entry in range(1, len(elements)):
        current_integer = elements[entry]
        if current_integer == previous_integer:
            continue
        elif current_integer < previous_integer:
            temp_direction = "down"
        elif current_integer > previous_integer:
            temp_direction = "up"
        if direction == "":
            direction = temp_direction
        if temp_direction != direction:
            number_of_direction_changes += 1
            direction = temp_direction
        previous_integer = current_integer
    return number_of_direction_changes


# ___________________________________________________________________________________
