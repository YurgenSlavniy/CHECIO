# ___________________________________________________________________________________
# Rectangle Perimeter >< 
# Как найти периметр прямоугольника ? 
# Undefined <>
# Russian math numbers --
# ___________________________________________________________________________________
# Undefined
# DE EN FR PL Russian UK ZH-HANS

# Функция должна принимать два положительных числа (length и width) в качестве входных данных и возвращать периметр прямоугольника.

# example
# Входные данные: Два целых числа (int).
# Выходные данные: Целое число (int).

# Примеры:
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18

# Как это может использоваться:

# -   в архитектурных и инженерных программах для вычисления периметров зданий или комнат;
# -   в компьютерной графике для вычисления периметра прямоугольника на экране;

# Предусловия:

#  - length, width ∈ R;
#  - length, width > 0.
# ___________________________________________________________________________________
def rectangle_perimeter(length: int, width: int) -> int:
    return (length + width) * 2


print("Example:")
print(rectangle_perimeter(3, 2))

# These "asserts" are used for self-checking
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18
assert rectangle_perimeter(1, 1) == 4
assert rectangle_perimeter(1, 5) == 12
assert rectangle_perimeter(4, 1) == 10
assert rectangle_perimeter(100, 100) == 400
assert rectangle_perimeter(0.5, 2) == 5
