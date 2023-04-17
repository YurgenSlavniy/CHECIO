# Median >< 
# Find the mathematical median in a list of numbers ? 
# Elementary+ <>
# Russian has-hints numbers statistics --
# ___________________________________________________________________________________
# Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины. 
# В сортированом массиве с нечётным числом элементов медиана — это число в середине массива. 
# Для массива с чётным числом элементов, где нет одного элемента точно посередине, 
# медиана — это среднее значение двух чисел, находящихся в середине массива.
# В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.

# Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Middle Characters.

# Входные данные: Массив как список (list) чисел (int).
# Выходные данные: Медиана как число (int, float).

# Примеры:
# assert checkio([1, 2, 3, 4, 5]) == 3
# assert checkio([3, 1, 2, 5, 3]) == 3
# assert checkio([1, 300, 2, 200, 1]) == 2
# assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

# Как это используется: Медиана находит свое применение в статистике и теории вероятности, 
# и особенно важна для ассиметричного распределения. 
# Для примера: мы хотим узнать среднее доход населения -- 100 человек получают $100 в месяц и 10 человек получают $1,000,000. 
# Если мы возьмем среднее арифметическое, то получим $91,000.
# Это довольно странное число, не показывающее истинного положения дел. 
# В этом случае медиана будет равна $100, 
# что станет для нас более полезной величиной и покажет более правдоподобную картину. Статья в Википедии.

# Предусловия:
# 1 < len(data) ≤ 1000
# all(0 ≤ x < 10 ** 6 for x in data)

# ___________________________________________________________________________________
# SOLUTION 15. <>
import numpy as np

def checkio(data: list[int]) -> int | float:
    return np.median(data)


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

# <><><><><> Best "Creative" Solution <><><><><>
checkio=lambda d:(lambda t,n:t[n]+t[-n-1])(sorted(d),len(d)//2)/2

# <><><><><> Best "Speedy" Solution <><><><><>
# Find the k'th-smallest value in a, worst case O(n)
# Skip the first d elements and consider only the next n
def select(a, d, n, k):
    if n <= 5:
        return sorted(a[d:d+n])[k]

    # Find median of medians of 5
    medians = [sorted(a[i:i+5])[2] for i in range(d, d+n-4, 5)]
    m = len(medians)
    median = select(medians, 0, m, m // 2)

    # Partition around the median.
    # a[d:i]     <= median
    # a[j+1:d+n] >= median
    i, j = d, d+n-1
    while i <= j:
        while a[i] < median: i += 1
        while a[j] > median: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if d+k < i: return select(a, d, i-d, k)
    else:       return select(a, i, n+d-i, k+d-i)

def checkio(data):
    n = len(data)
    if n % 2 == 1:
        return select(data, 0, n, n//2)
    else:
        return 0.5 * (select(data, 0, n, n//2-1) + select(data, 0, n, n//2))

# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List
import numpy as np

def checkio(data: List[int]) -> [int, float]:
    return np.median(data)

# <><><><><> Uncategorized <><><><><>
def checkio(data: list[int]) -> int | float:
    # replace this for solution
    m = 0
    m1 = 0
    m2 = 0
    data = sorted(data)
    #data.sort()
    if len(data) % 2 == 0:
        m1 = data[len(data) // 2 -1]
        m2 = data[len(data) // 2]
        m = (m1 + m2) /2
    else:
        m = data[len(data) // 2]
        
    return m

# ___________________________________________________________________________________
