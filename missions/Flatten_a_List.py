# Flatten a List >< 
# Make out Nicola's nested list and tweet how you did it ? 
# Simple+ <>
# Русский list parsing --
# ___________________________________________________________________________________
# Simple+
# DE EN HU Русский UK

# Никола любит классифицировать все вещи. Он классифицировал ряд чисел, 
# и в результате его усилий простая последовательность чисел стала глубоко вложенным списком. 
# София и Стефан не понимают, как он организовал числа, 
# и нужно выяснить, что всё это значит.
# Им нужна ваша помощь, чтобы понять сумасшедший список Николы.

# Существует список, который содержит целые числа или другие вложенные списки, 
# которые могут содержать ещё несколько списков и целых чисел, которые затем... 
# ну, вы поняли. Вы должны поместить все целые значения в один плоский список. 
# Порядок должен быть такой же, как и в первоначальном списке, 
# с представлением строки слева направо.

# Мы должны скрыть эту программу от Николы, сделав её маленькой и лёгкой. 
# Поэтому ваш код должен быть короче, чем 140 символов (с пробелами) .

# Входные данные: Вложенный список целых чисел.
# Выходные данные: Список или другой итерируемый обьект (кортеж, генератор, итератор) целых чисел.

# Примеры:
assert list(flat_list([1, 2, 3])) == [1, 2, 3]
assert list(flat_list([1, [2, 2, 2], 4])) == [1, 2, 2, 2, 4]
assert list(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]])) == [
    2,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
    7,
]
assert list(flat_list([-1, [1, [-2], 1], -1])) == [-1, 1, -2, 1, -1]

# Как это используется: Эта концепция полезна для разбора и анализа файлов 
# со сложной структурой и она бросает вызов вашей креативности в написании короткого кода.

# Предусловия:
# - 0 ≤ |array| ≤ 100;
# - ∀ x ∈ array : -232 < x < 232 or x is a list;
# - depth < 10.  
# ___________________________________________________________________________________
# SOLUTION <>
from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    r = []
    for i in array:
        if isinstance(i, list):
            r.extend(flat_list(i))
        else:
            r.append(i)
    return r


# <><><><><> Best "Clear" Solution <><><><><>
def flat_list(l):
    r = []
    def f(l):
        for i in l:
            r.append(i) if type(i) is int else f(i)
    f(l)
    return r
    

# <><><><><> Best "Creative" Solution <><><><><>
flat_list=f=lambda d:0*d==0 and[d]or sum(map(f,d),[])#)][,)d,f(pam(mus ro]d[dna 0==d*0:d adbmal=f=tsil_talf
#Tweet? Palindrome? Solution.


# <><><><><> Best "Speedy" Solution <><><><><>
def flat_list(array):
    import re
    return [int(i) for i in re.findall(r'[-]?\d+', str(array))]
    

# <><><><><> Best "3rd party" Solution <><><><><>
from pandas.core.common import flatten


def flat_list(array: list) -> list:
    """
        What flatten does, is to use recursion over the list until the list is completely flat.
          Since pandas is built on top of numpy, it means it's a fast solution
    """
    return list(flatten(array))


# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def flat_list(array: list[int]) -> Iterable[int]:
    res = []
    for i in array:
        if type(i) == list:
            res.extend(flat_list(i))
        else:
            res.append(i)
    return res



# ___________________________________________________________________________________
