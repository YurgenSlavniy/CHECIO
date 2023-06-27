# The Most Frequent >< 
# Определите наиболее часто встречающийся элемент в последовательности. ? 
# Elementary <>
# Russian has-hints list statistics --
# ___________________________________________________________________________________
# Elementary
# EN JA Russian UK ZH-HANS
# Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.

# Входные данные: список строк.
# Выходные данные: строка.

# Примеры:
# assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
# assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

# ___________________________________________________________________________________
# SOLUTION 19. <>
def most_frequent(data: list[str]) -> str:
    return max(set(data), key=data.count)
    
print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"


# <><><><><> Best "Clear" Solution <><><><><>
from statistics import mode as most_frequent


# <><><><><> Best "Creative" Solution <><><><><>
def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key = data.count)


# <><><><><> Best "Speedy" Solution <><><><><>
def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    mx = 0
    word = ''
    for s in set(data):
        if data.count(s) > mx:
            mx = data.count(s)
            word = s
    return word


# <><><><><> Best "3rd party" Solution <><><><><>
def most_frequent(data: list) -> str:
    """pandas"""
    import pandas as pd

    if not data : return ''
    df = pd.DataFrame(data, columns=['valeurs'])
    dg = df['valeurs'].value_counts()


    return dg.index[0]


# <><><><><> Uncategorized <><><><><>
from collections import Counter
def most_frequent(data: list[str]) -> str:
    dictionary = Counter(data) 
    max_value = 0
    for iterable in dictionary:
        if dictionary[iterable] > max_value:
            max_value = dictionary[iterable]
            max_key = iterable 
    return max_key

# ___________________________________________________________________________________
