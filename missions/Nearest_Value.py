# ___________________________________________________________________________________
# Nearest Value ><   
# Find the nearest value to the given one. ?
# Elementary+ <> 
# Set Array --
# ___________________________________________________________________________________
# Elementary+
# PL EN JA Russian

# Найдите ближайшее значение к переданному.
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.

# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.

# Несколько уточнений:

# - Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# - Ряд чисел всегда не пустой, т.е. размер >= 1;
# - Переданное значение может быть в этом ряде, а значит оно и является ответом;
# - В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# - Ряд не отсортирован и состоит из уникальных чисел.

# Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
# Выходные данные: Int.

# Пример:
# nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7

# ___________________________________________________________________________________
# SOLUTION <>
def nearest_value(values: set, one: int) -> int:
    values = list(values)
    if one in values:
        return one
    else:
        values.append(one)
        values.sort()
        ind = values.index(one)
        if ind == 0:
            return values[1]
        elif ind == len(values) - 1:
            return values[-2]
        else:
            prev = values[ind - 1]
            next = values[ind + 1]
            d_prev = one - prev
            d_next = next - one
            if d_next == d_prev:
                return prev
            elif d_prev < d_next:
                return prev
            else:
                return next
               
# <><><><><> Best "Clear" Solution <><><><><>    
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))

# <><><><><> Best "Creative" Solution <><><><><> 
def nearest_value(values: set, one: int) -> int:   
    return min(sorted(values), key = lambda i: abs(i - one)) 

# <><><><><> Best "Speedy" Solution <><><><><> 
from functools import cmp_to_key
def nearest_value(values: set, one: int) -> int:    
    return sorted(values, key = cmp_to_key(lambda a,b: abs(a - one) - abs(b - one) or (a-b)))[0]

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def nearest_value(values: set, one: int) -> int:
    value_list = np.array(list(values))
    value_list.sort()
    index = abs(value_list - one).argmin()
    return value_list[index]

# <><><><><> Uncategorized <><><><><> 
def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    x=list(values)
    x.append(one)
    x.sort()
    index=x.index(one)
    if one==(x[0]):
        return x[index+1]
    elif one==(x[-1]):
        return x[index-1]        
    elif (x[index]-x[index-1]) < (x[index+1]-x[index]):
        return x[index-1]
    elif (x[index]-x[index-1]) > (x[index+1]-x[index]):
        return x[index+1]
    elif x[index-1] < x[index+1]:
        return x[index-1]
    elif x[index-1] > x[index+1]:
        return x[index+1]