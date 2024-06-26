# Quadratic Equation Roots >< 
# Let's dig up roots ? 
# Undefined <>
# math numbers  --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# A quadratic equation is represented as ax2 + bx + c = 0. 
# The general formula to find its roots (x-values for which y = 0) is:

# This formula provides two roots: x1, x2. 
# The value inside the square root, b2-4ac is known as the discriminant (D).
# Based on the value of the discriminant, a quadratic equation can have:

# - two distinct real roots (D > 0);
# - one real root (D = 0);
# - no real roots (D < 0).

# Your code must return Iterable containing two values: the roots x1, x2, 
# sorted descending. If there's only one real root, both values will be the same. 
# If there are no real roots, the Iterable should contain the string "No real roots".

# Input: Three integers (int).
# Output: Tuple or other Iterable of two numbers (int|float) or string (str). 
 
# Examples:
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]

# How it’s used: this function can be useful in mathematical computations, 
# physics simulations, optimization problems, or anywhere quadratic equations are utilized.

# Preconditions:
# - a != 0;
# - -109 <= a, b, c <= 109.
# ___________________________________________________________________________________
# SOLUTION <>
from collections.abc import Iterable
from typing import Union
import numpy as np


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + np.sqrt(discriminant)) / (2*a)
        x2 = (-b - np.sqrt(discriminant)) / (2*a)
        return sorted([x1, x2], reverse=True)
    elif discriminant == 0:
        x = -b / (2*a)
        return [x, x]
    else:
        return ["No real roots"]

print("Example:")
print(list(quadratic_roots(1, 2, 3)))

# These "asserts" are used for self-checking
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

# <><><><><> Best "Clear" Solution <><><><><>
from collections.abc import Iterable


def quadratic_roots(a: int, b: int, c: int):
    det = b*b - 4*a*c
    return ['No real roots'] if det < 0 else [(-b + det**0.5)/2/a, (-b - det**0.5)/2/a]

# <><><><><> Best "Creative" Solution <><><><><>
from collections.abc import Iterable
from math import sqrt


def quadratic_roots(a: int, b: int, c: int) -> Iterable[int | str]:
    d = (b**2) - 4 * a * c
    return ["No real roots"] if d < 0 else [((-b) + sqrt(d)) / (2 * a), ((-b) - sqrt(d)) / (2 * a)]

# <><><><><> Best "Speedy" Solution <><><><><>
from collections.abc import Iterable
from typing import Union


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:

    return [(-b+(b**2-4*a*c)**0.5)/(2 * a), (-b-(b**2-4*a*c)**0.5)/(2 * a)] if (b ** 2 - 4 * a * c) >= 0 else ["No real roots"]


# <><><><><> Best "3rd party" Solution <><><><><>
from collections.abc import Iterable
import numpy as np


def quadratic_roots(a: int, b: int, c: int) -> Iterable[int | str]:
    d = b**2-4*a*c
    if d > 0:
         return [int(-1 * b + np.sqrt(d))/(2*a), int(-1*b - np.sqrt(d))/(2*a)]
    elif d == 0:
         return [-1*b//(2*a)]*2
    else:
         return ['No real roots']

# <><><><><> Uncategorized <><><><><>
 Quadratic Equation Roots
magi 2023-2025

11 Maciej_Biegaj
[Follow]
from collections.abc import Iterable
from typing import Union
from math import sqrt

def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b + sqrt(disc)) / (2*a)
        x2 = (-b - sqrt(disc)) / (2*a)
        return sorted([x1, x2], reverse=True)
    elif disc == 0:
        x = -b / (2*a)
        return [x, x]
    else:
        return ['No real roots']
    return []


# ___________________________________________________________________________________
