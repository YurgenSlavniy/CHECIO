# Changing direction >< 
# Find how many times the sorting directions was changed ? 
# Simple <>
# Russian list logic --
# ___________________________________________________________________________________
# Дан список состоящий из целых чисел. 
# Ваша задача выяснить сколько раз в нем меняется направление при переходе от одного числа к другому.
# Если числа равны, то направление не меняется. 
# В случае, если следующий элемент отличается от предыдущего - необходимо определить в какую сторону поменялось направление.

# Давайте взглянем на схему:
# [1,2,2,1,2,2]

# На ней изображено следующее:

# - для фрагмента 1, 2, 2 - направление идет вверх;
# - для фрагмента 2, 1 - идет вниз;
# - для фрагмента 1, 2, 2 - снова возрастает.

# Так что в данном примере есть всего две точки смены направления:
# 1 - направление меняется с возрастающего на убывающее, 
# и #2 - наоборот, начинает опять расти вверх.

# Входные данные: Список целых чисел.
# Выходные данные: Целое число.

# Примеры:

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

# Preconditions:
# Список не может быть пустым;
# Все элементы в списке являются положительными целыми числами.
# ___________________________________________________________________________________
# SOLUTION 23. <>
def changing_direction(elements: list) -> int:
    
    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')
    
    return len(dirs) - bool(dirs)

print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
