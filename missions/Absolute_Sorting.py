# Absolute Sorting >< 
# How to sort an array by absolute values ? 
# Elementary  <>
# Russian has-hints list numbers --
# ___________________________________________________________________________________
#  Давайте посмотрим на сортировку. Дан массив с особыми правилами.

# Массив (a list) содержит различные числа. Вам необходимо отсортировать их, 
# но отсортировать на основе абсолютных значений в возрастающем порядке. 
# Для примера, последовательность (-20, -5, 10, 15) 
# будет отсортирована следующим образом (-5, 10, 15, -20). 
# Ваша функция должна возвращать список (list) или кортеж (tuple).

# Входные данные: Массив чисел как кортеж (tuple).
# Выходные данные: Список (list) или кортеж (tuple) (но не генератор) отсортированный по абсолютным значениям чисел.

# Дополнение: Результат вашей функции вы увидите как список (list) в панели выводов результатов проверки.

# Примеры:
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

# Зачем это нужно: Сортировка это часть очень многих задач, так что будет полезно понимать, как ее использовать.

# Предусловия: len(set(abs(x) for x in array)) == len(array)
# 0 < len(array) < 100
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# ___________________________________________________________________________________
# SOLUTION 24. <>
def checkio(values: list) -> list:
    return sorted(values, key=abs)

print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(numbers_array):
    """
    The magic of the key :)
    """
    return tuple(sorted(numbers_array, key=abs))

# <><><><><> Best "Creative" Solution <><><><><>
from functools import partial as c
checkio=c(sorted,key=abs)

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(numbers_array):
    b=sorted(numbers_array, key=lambda x:(abs(x)))
    return b

# <><><><><> Best "3rd party" Solution <><><><><>
def checkio(numbers_array):
    import numpy
    D=numpy.array(numbers_array)
    return(D[numpy.argsort(numpy.absolute(D))].tolist()) # also handles absolute value of complex numbers
    

# <><><><><> Uncategorized <><><><><>
from collections import OrderedDict

def checkio(numbers):
    sorted_dict = OrderedDict(sorted({num: abs(num) for num in numbers}.items(), key=lambda x: x[1]))
    return list(sorted_dict.keys())
# ___________________________________________________________________________________
