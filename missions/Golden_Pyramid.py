# Golden Pyramid >< 
# Help Stephen find the best route down a pyramid ? 
# Elementary+ <>
# has-hints math numbers --
# ___________________________________________________________________________________
#  Elementary+

# Нашему Робо-Трио необходимо тренироваться для будущих приключений и охоты за сокровищами 
# (золотые контакты нужны всем). Стефан построил специальную упрощенную модель пирамиды. 
# И теперь наши роботы будут тренироваться в забегах за золотом на скорость. 
# Они начинают с вершины пирамиды и собирают золото в каждой комнате, 
# через которую проходят. В каждой комнате они выбирают влево или вправо и спускаются на следующий уровень. 
# Чтобы оценивать результаты, Стефану нужно знать, а сколько максимум можно собрать за один забег.

# Представьте список списков в котором первый список имеет одно число и следующие на одно число больше чем предыдущий. 
# Такой список списков будет выглядеть как пирамида.
# Тебе нужно написать функцию, которая поможет Стефану найти максимальную сумму золота на самом выгодном маршруте 
# с вершины пирамиды до ее основания. 
# Все маршруты прохода по пирамиде из шагов вниз и влево/вправо.

# Примечания: Попробуйте думать о шаге вниз-влево, как о движении в следующий ряд не изменяя индекс в ряду и о шаге вниз/вправо -
# - с увеличением индекса в ряду на единицу. Будьте осторожны если вы хотите решать задачу рекурсией. 
# получится медленное решение.

# Ввод: Пирамида, как список списков. Каждый список целых чисел.
# Вывод: Максимально количество золота за один забег, как целое число.

# Примеры:
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)

# Связь с реальной жизнью: Эта классическая задача может помочь вам освоить динамическое программирование. 
# Также это может пригодится вам для решения многих оптимизационных задач.

# Предусловия:
# -    0 < len(pyramid) ≤ 20;
# -   all(all(0 < x < 10 for x in row) for row in pyramid).
 

# ___________________________________________________________________________________
# SOLUTION <>
def count_gold(pyramid: list[list[int]]) -> int:
    
    
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
            
    return pyramid[0][0]
    

print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)

# These "asserts" are used for self-checking
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)
assert (
    count_gold(
        [
            [4],
            [3, 0],
            [5, 1, 1],
            [2, 0, 2, 0],
            [1, 1, 1, 8, 3],
            [5, 3, 4, 8, 2, 8],
            [1, 0, 5, 0, 4, 3, 1],
        ]
    )
    == 30
)
assert (
    count_gold(
        [
            [6],
            [7, 9],
            [3, 8, 3],
            [3, 4, 0, 2],
            [6, 9, 9, 6, 8],
            [3, 7, 0, 8, 2, 2],
            [0, 6, 3, 0, 0, 6, 7],
        ]
    )
    == 49
)
assert (
    count_gold(
        [
            [6],
            [0, 6],
            [3, 0, 7],
            [0, 4, 2, 9],
            [4, 4, 3, 6, 9],
            [3, 1, 0, 5, 9, 0],
            [8, 9, 7, 7, 3, 4, 5],
        ]
    )
    == 50
)
assert (
    count_gold(
        [
            [6],
            [6, 9],
            [7, 1, 4],
            [6, 9, 9, 7],
            [1, 6, 7, 9, 7],
            [5, 7, 2, 6, 0, 9],
            [1, 2, 2, 6, 0, 1, 6],
            [8, 5, 0, 3, 1, 4, 3, 1],
            [9, 6, 4, 1, 1, 9, 3, 7, 9],
            [5, 8, 4, 3, 5, 4, 5, 1, 8, 3],
        ]
    )
    == 66
)

print("The mission is done! Click 'Check Solution' to earn rewards!")


# <><><><><> Best "Clear" Solution <><><><><>
def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    
    '''
    
    ===============
    Golden Pyramid
    ===============
    
    Approach
    --------
    
    This algorithm is a greedy approach to solving the problem.  
    Instead of working forward through the pyramid, we will work backwards.
    The idea is to start in the second to bottom row and select maxium of the
    the next two possible values from the current node and add that value to 
    the current node.
    
    After that we continue to roll up the rows and repeat the process for each
    node in that row.  When we reach the starting node we will have the sum
    of the maximum path.  
    
    *Note*: we are not finding the best path; we are only finding the maxium sum 
    from that path.  

    Code
    ----
    
    I want a mutable copy of the pyramid to work with.  
    Get the number of rows from the **len** function.  
    The last row is not in play to start hence **rows-1**
    Also we're working backwards so use the **reversed** function.
    Need to itertate over each item in the row. Note the plus 1, range(0) 
    returns an empty list.
    The possible nodes to examine are 1) the on directly below i+1,j
    and the one below and to the right i+1, j+1.  We use the **max** 
    function to select the largest one and then add it to the current
    node.  
    
    '''
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py)-1)):   
        for j in range(i+1):
            py[i][j] +=(max(py[i+1][j], py[i+1][j+1]))

    return py[0][0]


# <><><><><> Best "Creative" Solution <><><><><>
count_gold=lambda p:__import__("functools").reduce(lambda D,r:[x+max(D[j],D[j+1])
for j,x in enumerate(r)],p[-2::-1],list(p[-1]))[0]


# <><><><><> Best "Speedy" Solution <><><><><>
def count_gold(pyramid):
    p = tuple(map(list, pyramid))
    for i in reversed(range(len(p))):
        for j in range(i): p[i-1][j] += max(p[i][j:j+2])
    return p[0][0]


# <><><><><> Best "3rd party" Solution <><><><><>
import numpy
def count_gold(pyramid):
    l = len(pyramid)-1
    zv = [list(format(x, '0'+str(l)+'b')) for x in range(2**l)]
    im = [[0]+list(numpy.cumsum([int(x) for x in l])) for l in zv ]
    ms = max([sum([x[i] for i,x in zip(iv,pyramid)]) for iv in im])
    return ms


# <><><><><> Uncategorized <><><><><>
def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    routes = [(0 ,pyramid[0][0])] # make list of current_index, sum_gold pairs
    for level in pyramid[1:]:
        newroutes = []
        for current_index, sum_gold in routes:
            newroutes.append((current_index, sum_gold + level[current_index]))
            newroutes.append((current_index+1, sum_gold + level[current_index+1]))
        routes = newroutes
            
    return max(routes, key = lambda route: route[1])[1]


# ___________________________________________________________________________________
