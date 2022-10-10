# ___________________________________________________________________________________ 
# Sum by Type >< 
# Values should be summed differently for different types? 
# Elementary+ <>
# List string iter Array Int --
# ___________________________________________________________________________________
# Elementary+
# English UK

# You have a list. Each value from that list can be either a string or an integer.
# Your task here is to return two values. The first one is a concatenation of all strings from the given list.
# The second one is a sum of all integers from the given list.

# Input: A list of strings and integers.
# Output: A list or tuple.

# Examples:
# assert list(sum_by_types([])) == ["", 0]
# assert list(sum_by_types([1, 2, 3])) == ["", 6]
# assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
# assert list(sum_by_types(["1", "2", 3])) == ["12", 3]

# How it’s used: Input the values of different types and different operations with them,
# depending of type, is the usual thing in development.

# ___________________________________________________________________________________
# SOLUTION <>
from typing import Tuple

def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    ints = 0
    strs = ''
    for item in items:
        if type(item) is int:
            ints += item
        else:
            strs += item
    return (strs, ints)

print("Example:")
print(list(sum_by_types([])))

assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]

# <><><><><> Best "Clear" Solution <><><><><>
def sum_by_types(items):
    result = ['', 0]
    for item in items:
        result[isinstance(item, int)] += item
    return result

# <><><><><> Best "Creative" Solution <><><><><>
import collections, operator
class Neutral(dict): __missing__ = staticmethod(lambda T: T())
report = operator.itemgetter(str, int)

def sum_by_types(a: list) -> report:
    accum = Neutral()
    for elem in a: accum[type(elem)] += elem
    return report(accum)

# <><><><><> Best "Speedy" Solution <><><><><>
from typing import List, Tuple

def sum_by_types(items: List) -> Tuple[str, int]:
    result = ['', 0]
    for item in items:
        result[type(item)==int] += item
    return tuple(result)

# <><><><><> Uncategorized  <><><><><>
def sum_by_types(items):
    str_conc = ''
    int_sum = 0
    for i in items:
        if type(i) == str:
            str_conc = str_conc + i
        else:
            int_sum = int_sum + i       
    return [str_conc, int_sum]
