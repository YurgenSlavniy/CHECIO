# ___________________________________________________________________________________ 
# All the Same >< 
# Check if all elements are the same ? 
# Simple <>
# List logic --
# ___________________________________________________________________________________
# Simple
# EN JA Russian UK ZH-HANS

# We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. 
# In order to see all other solutions you should change the filter.
# В этой миссии Вам надо определить, все ли элементы массива равны.

# Входные: List.
# Выходные: Bool.

# Примеры:
# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

# Precondition: all elements of the input list are hashable
# ___________________________________________________________________________________
# SOLUTION <>
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 0 or len(elements) == 1:
        return True
    else:
        set_elements = set(elements)
        if len(set_elements) == 1:
            return True
        else:
            return False
        
if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    
# <><><><><> Best "Creative" Solution <><><><><>
all_the_same = lambda e: e[1:] == e[:-1]

# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List, Any
from numpy import unique

def all_the_same(elements: List[Any]) -> bool:
    return len(unique(elements)) <= 1

# <><><><><> Uncategorized  <><><><><>
def all_the_same(elements: List[Any]) -> bool:
    len_elements = len(elements)
    if len_elements == 0:
        return True
    else:
        for i in elements:
            same = elements.count(i)
        
            if same < len_elements:
                return False
            else:
                return True
            
# <><><><><> Clear <><><><><>
from operator import eq
from itertools import starmap

def all_the_same(elements):
    return all(starmap(eq, zip(elements, elements[1:])))