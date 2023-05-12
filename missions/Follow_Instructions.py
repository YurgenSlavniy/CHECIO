# Follow Instructions >< 
# Cледуйте инструкциям, чтобы найти конечные координаты ? 
# Elementary+ <>
# Russian parsing pathfinding string --
# ___________________________________________________________________________________
# Elementary+
# EN Russian UK
# Вы получили письмо от друга, которого вы не видели и не слышали какое-то время. 
# В этом письме он дает вам указания о том, как найти скрытое сокровище!

# В этой миссии Вы должны следовать данному списку инструкций,
# которые приведут вас к определенной точке на карте. 
# Список инструкций - это строка, каждая буква этой строки указывает Вам направление следующего шага.
# Буква «f» - указывает на то, что Вам нужно двигаться вперед, «b» - назад, «l» - влево, а «r» - вправо.
# То есть, если список Ваших инструкций - «fflff», то Вы должны сделать два шага вперед, 
# потом один шаг влево, а затем снова переместиться на два шага вперед.
# Теперь давайте представим, что Вы находитесь в позиции (0, 0). 
# Продвинувшись вперед, Вы измените свою позицию на (0, 1). 
# Сделав еще один шаг, она будет (0, 2). Ступив влево, Ваша позиция станет (-1, 2). 
# И после последующих двух шагов вперед Ваши координаты будут (-1, 4).

# Ваша цель заключается в том, чтобы найти конечные координаты.
# Точно так же, как в приведенном выше примере они были (-1, 4).

# Входные данные: Строка.
# Выходные данные: A tuple (или список) из двух ints.

# Примеры:
# assert list(follow("fflff")) == [-1, 4]
# assert list(follow("ffrff")) == [1, 4]
# assert list(follow("fblr")) == [0, 0]

# Как это используется: в играх, где есть карта.
# Предварительное условие: Допускаются только символы f, b, l и r

# ___________________________________________________________________________________
# SOLUTION 18. <>
def follow(instructions: str) -> tuple[int, int] | list[int]:
    x = 0
    y = 0
    for el in instructions:
        if el == 'f':
            y += 1
        elif el == 'b':
            y -= 1
        elif el == 'l':
            x -= 1
        else:
            x += 1
    return tuple([x, y])

print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]


# <><><><><> Best "Clear" Solution <><><><><>
follow = lambda i: [i.count(x)-i.count(y) for x, y in ('rl', 'fb')]

# <><><><><> Best "Creative" Solution <><><><><>
from collections import Counter
from typing import Tuple


def follow(instructions: str) -> Tuple[int]:
    count = Counter(instructions)
    return (count['r'] - count['l'], count['f'] - count['b'])

# <><><><><> Best "Speedy" Solution <><><><><>
import numpy as np

step = {'f': [0, 1], 'l': [-1, 0], 'b': [0, -1], 'r': [1, 0]}

def follow(instructions):
    return np.sum([step[i] for i in instructions], axis=0).tolist()

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

step = {'f': [0, 1], 'l': [-1, 0], 'b': [0, -1], 'r': [1, 0]}

def follow(instructions):
    return np.sum([step[i] for i in instructions], axis=0).tolist()

# <><><><><> Uncategorized <><><><><>
def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    ls = [0, 0]
    for i in instructions:
        if i == 'f':
            ls[1] += 1
        if i == 'b':
            ls[1] -= 1
        if i == 'r':
            ls[0] += 1
        if i == 'l':
            ls[0] -= 1

    return ls

# ___________________________________________________________________________________
