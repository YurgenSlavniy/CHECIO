# ___________________________________________________________________________________. 
# Remove All Before ><   
# Remove all the elements before the given one from the array. ?
# Elementary <> 
# Array numbers --
# ___________________________________________________________________________________
# Elementary
# EN JA UK PL Russian

# Не все элементы важны. Вам нужно удалить из списка все элементы до указаного.

# На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.
# Есть два ньюанса: 
# - (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен измениться. 
# - (2) если list пустой, то он должен остаться пустым.

# Входные данные: Список и элемент до которого нужно удалить другие элементы.
# Выходные данные: Набор значений (кортеж, список, итератор ...).

# Пример:
# remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
# remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
# ___________________________________________________________________________________
# SOLUTION <>
from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items or items == [] or items[0] == border:
        return items  
    else:
        for i in items:
            if i == border:
                a = items.index(i)
                return items[a:]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
               
# <><><><><> Best "Clear" Solution <><><><><>     
def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items
    
# <><><><><> Best "Creative" Solution <><><><><>  
remove_all_before=lambda i,b:b in i and i[i.index(b):] or i

# <><><><><> Best "Speedy" Solution <><><><><>  
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items

# <><><><><> Best "3rd party" Solution <><><><><>  
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    import numpy    
    arr=numpy.array(items)
    try:
        i=list(arr).index(border)
        b=i
    except ValueError :
        b=0
    return arr[b:]