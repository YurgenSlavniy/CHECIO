# ___________________________________________________________________________________ 
# Even the Last >< 
# How to work with arrays indexes. ? 
# Elementary <>
# Russian math numbers has-Hints --
# ___________________________________________________________________________________
# Elementary
# DE ES HU IT PT-BR Russian ZH-HANS FR FA PL PT UK EN JA EL

# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), 
# затем перемножить эту сумму и последний элемент исходного массива. 
# Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).

# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int).

# Примеры:

# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0

# Зачем это нужно: Индексы и срезы - очень важные элементы программирования,
# как на Python, так и на других языках. Это поможет вам в дальнейшем.

# Предусловия: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# ___________________________________________________________________________________
# SOLUTION <>

def checkio(array):
#    from numpy import sum
    if len(array) > 0:
        return int(sum(array[::2])*array[-1])
    else:
        return 0
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    
# <><><><><> Best "Clear" Solution <><><><><>
def checkio(array):
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

# <><><><><> Best "Creative" Solution <><><><><>
checkio = lambda array: sum(array[::2]) * sum(array[-1:])

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(array):
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0

# <><><><><> Best "3rd party" Solution <><><><><>
def checkio(array):
    from numpy import sum
    if len(array) > 0:
        return int(sum(array[::2])*array[-1])
    else:    
        return 0