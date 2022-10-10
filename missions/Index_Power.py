# ___________________________________________________________________________________
# Index Power ><   
# What is the power hidden within indexes?
# Elementary <> 
# List numbers has-Hints --
# ___________________________________________________________________________________
# Elementary
# CS ES FR IT PL EN DE EL FA JA PT-BR Russian UK

# Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. Если N за границами массива, тогда вернуть -1. Не забывайте, что первый элемент имеет индекс 0.

# Давайте посмотрим на несколько примеров:
# - массив = [1, 2, 3, 4] и N = 2, тогда результат 3 2 == 9;
# - массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.

# Входные значения: Два агумента. Массив как список целых и число как целое.
# Выходные значения: Целое число.

# Пример:
# index_power([1, 2, 3, 4], 2) == 9
# index_power([1, 3, 10, 100], 3) == 1000000
# index_power([0, 1], 0) == 1
# index_power([1, 2], 3) == -1

# Как это используется: Эта миссия учит вас как использовать основы массивов и индексов в объединении с простой математикой.

# Предусловие: 0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)
# ___________________________________________________________________________________
# SOLUTION <>
def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n]**n
    else:
        return -1

if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
               
# <><><><><> Best "Clear" Solution <><><><><>   
def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1
    
# <><><><><> Best "Creative" Solution <><><><><> 
index_power=lambda a,n:-(len(a)<=n)or a[n]**n

# <><><><><> Best "Speedy" Solution <><><><><> 
def index_power(array, n):
    return array[n]**n if len(array) > n else -1

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def index_power(array, n):
    a=None
    if n>(len(array)-1):
        a=-1
    else:
        a=np.power(array[n],n)
        
    return int(a)

# <><><><><> "Creative" Solution <><><><><>
def index_power(ra, n):
    return {i: ra[i]**i for i in range(len(ra))}.get(n, -1)
