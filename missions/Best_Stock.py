# ___________________________________________________________________________________ 
# Best Stock ><   
# Find the nearest value to the given one?
# Elementary+ <> 
# Math has-Hints --
# ___________________________________________________________________________________
# Elementary+
# EN JA Russian

# Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.

# Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)
# Output: Строка, рыночный код

# Example:
# best_stock({
#    'CAC': 10.0,
#    'ATX': 390.2,
#    'WIG': 1.2
#  }) == 'ATX'
# best_stock({
#    'CAC': 91.1,
#    'ATX': 1.01,
#    'TASI': 120.9
# }) == 'TASI'
# ___________________________________________________________________________________
# SOLUTION <>
def best_stock(data: dict) -> str:
    a = max(data.values())
    for key, val in data.items():
        if val == a:
            return key

if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
               
# <><><><><> Best "Clear" Solution <><><><><> 
def best_stock(data):
    return max(data, key=data.__getitem__)

# <><><><><> Best "Creative" Solution <><><><><> 
best_stock = lambda d: next(x for x in d if d[x] == max(d.values()))

# <><><><><> Best "Speedy" Solution <><><><><> 
def best_stock(data):
    return max(data, key=data.get)

# <><><><><> Best "3rd party" Solution <><><><><> 
# -*- coding:utf-8 -*-
import pandas as pd
def best_stock(data):
    return(pd.Series(data).idxmax())