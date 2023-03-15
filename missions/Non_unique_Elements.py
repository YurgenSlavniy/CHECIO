# ___________________________________________________________________________________ 
# Non-unique Elements ><   
# Trim an array down to its non-unique elements ?
# Elementary+  <> 
# Parsing has-Hints --
# ___________________________________________________________________________________
# Elementary+
# EN DE EL ES FR JA KO ZH-HANS HU PT-BR Russian UK
# We have prepared a set of Editor's Choice Solutions. 
# You will see them first after you solve the mission. 
# In order to see all other solutions you should change the filter.

# Дан непустой массив целых чисел (X). 
# В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. 
# Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). 
# Для решения этой задачи не меняйте оригинальный порядок элементов.
# Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].

# non-unique-elements
# Вх. данные: Список (list) целых чисел (int).
# Вых. данные: Итератор (an iterable) целых чисел (int).

# Пример:
# checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
# checkio([1, 2, 3, 4, 5]) == []
# checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
# checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

# Как это используется: Эта задача поможет вам понять, как манипулировать массивами. 
# Это полезный базис для решения более сложных задач. 
# Также эта идея может быть легко обобщена для реальных задач. 
# Для примера: если вам необходимо очистить статистику от редко встречающихся элементов (шум).

# Предусловия:
# 0 < len(data) < 1000
# ___________________________________________________________________________________
# SOLUTION <>
def checkio(data: list) -> list:
    count = []
    result = []
    for i in data:
        count.append(data.count(i))
    for i in range(len(count)):
        if count[i] != 1:
            result.append(data[i])
    return result

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
               
# <><><><><> Best "Clear" Solution <><><><><>   
checkio=lambda d:[x for x in d if d.count(x)>1]

# <><><><><> Best "Creative" Solution <><><><><>  
checkio = lambda d: list(filter(lambda i: d.count(i) - 1, d))

# <><><><><> Best "Speedy" Solution <><><><><>  
def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy

def checkio(data):
    counts = dict(list(zip(*numpy.unique(data, return_counts=True))))
    return [v for v in data if counts[v] > 1]

# <><><><><> Uncategorized  <><><><><>  
def checkio(data: list) -> list:
    for i in range(len(data),0,-1):
        if data.count(data[i-1]) <= 1:
            data.pop(i-1)
    return data
# ___________________________________________________________________________________
