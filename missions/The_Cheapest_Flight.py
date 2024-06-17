# The Cheapest Flight >< 
# Найти самый дешёвый перелёт ? 
# Simple <>
# list --
# ___________________________________________________________________________________
# «Нам нужно долететь домой как можно дешевле, 
# чтобы больше денег осталось на подарки. Тётя Лида просила сыров разных, 
# а Вася хотел машинку новую. Я уже довольно долго смотрю на расписание, 
# и мне начинает казаться, что некоторые самолёты летают зря.»

# На входе вы получаете расписание самолётов в виде списка, 
# каждый элемент которого — это цена прямого воздушного соединения двух городов
# (список из 3 элементов: первые два — названия городов в виде строк, и третий — цена перелёта).

# Самолёты летают в обе стороны и цена в обе стороны одинаковая. 
# Есть вероятность, что соединения между городами может и не быть.

# Найдите цену самого дешёвого перелёта для городов, 
# которые переданы 2-м и 3-м аргументами.
# Если перелет невозможен, верните 0

# Входные данные: 3 аргумента: расписание перелётов в виде списка списков, 
# город вылета, город назначения как строки.

# Выходные данные: Лучшая цена как целое число.

# Примеры:
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)

# Как это используется: может быть использовано в повседневной жизни для нахождения оптимальной комбинации.

# Предусловия:

# -    цена всегда целое число;
# -    в расписании рейсов есть хотя бы один элемент;
# -    оба искомых города есть в расписании.
# ___________________________________________________________________________________
# SOLUTION <>
def cheapest_flight(flights: list, start: str, end: str) -> int:

    graph = {}
    for flight in flights:
        city1, city2, price = flight
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = price
        graph[city2][city1] = price

    if start not in graph or end not in graph:
        return 0

    visited = {start: 0}
    to_visit = [start]

    while to_visit:
        current_city = to_visit.pop(0)
        for neighbor, price in graph[current_city].items():
            total_price = visited[current_city] + price
            if neighbor not in visited or total_price < visited[neighbor]:
                visited[neighbor] = total_price
                to_visit.append(neighbor)

    return visited.get(end, 0)



def cheapest_flight(costs: list, a: str, b: str) -> int:
    graph = {} # создали пустой словарик

    for cost in costs:  #  перебераем расписание самолётов в виде списка [["A", "C", 40], ["A", "B", 20],["A", "D", 20]...]
        a, b, price = cost # определяем переменные a - город вылета, b - город прилёта, price - цена перелёта. 
         # И присваиваем им значения из списка cost [a = "A", b = "C", price = 40]   
        if a not in graph: # Если город вылета из переменной a не в словаре graph, а если в словаре уже есть город вылета а , то ничего не добавляем идём дальше          
            graph[a] = {} # Добавляем в ранее созданный пустой список ключ - город вылета a = "A", а значением ей присваиваем пустой словарь {"A": {}} 
        if b not in graph: # Если город прилёта из переменной b не в словаре graph, если в словаре - дальше, ничего не добавив!  
            graph[b] = {} # Добавляем в ранее созданный пустой список ключ - город прилёта b = "С", а значением ей присваиваем пустой словарь {"С": {}} 
        graph[a][b] = price # в словаре graph, куда уже ранее поместили наши ключи {"A": {}}, помещаем значения [b] = price ранее пустое значение ключа => {"A": {"С": 40}}
        graph[b][a] = price # в словаре graph, куда уже ранее поместили наши ключи {"С": {}}, помещаем значения [a] = price ранее пустое значение ключа => {"С": {"A": 40}}
                
        # В итоге мы получили словарь со словарями, заполненный, относительно всего списка рейсов costs: list
        # в данном словаре первый ключ - это город. Значение это словарь в котором данными будет словарь с : ключ - город куда можно прилететь, значение - стоимость перелёта. 
        
    if a not in graph or b not in graph: # если в нашем словаре нет города вылета a или города прилёта b 
        return 0   # возвращаем нолик
    
    visited = {a: 0} # создаём словарь ключём которого будет город вылета a, а значением будет изначально 0
    to_visit = [a]  # создаём список, в который пока что помещается только город вылета a
        
    while to_visit: # пока существует список to_visit, заданный выше мы проваливаемся в бесконечный цикл
        current_city = to_visit.pop(0) #  определяем переменную в которую помещаем значение. Значением является to_visit.pop(0) - 
        # элемент под индексом 0, который забирается из списка to_visit. город вылета. 
        for neighbor, price in graph[current_city].items(): # берём наш словарь, и найдя там current_city, изначально это город вылета
            # мы значения этого ключа, другие словари. берём из этих словарей ключ - neighbor (город куда летает) и значение - price цена перелёта
            total_price = visited[current_city] + price # Общая цена , складывается из visited[current_city] - это созданный словарь чуть ранее,
            #  в котором current_city - изначально город откуда вылетели + price - цена перелёта
            if neighbor not in visited or total_price < visited[neighbor]: # Если город куда прилетаем не в списке посещённых городоа
            # или последняя цена ниже чем цена из словаря visited[neighbor]
                visited[neighbor] = total_price # присваиваем общую цену , добавляем в созданный словарик visited - последний город который посетили 
                # и цену которую за перелёт заплатили total_price
                to_visit.append(neighbor) #  в список посещённых городов, добавляем последний куда прилетели neighbor

    return visited.get(b, 0) # из словаря с посещёными городами методом  get находим если есть конечный город, куда должны прилететь b
    # а если не найдём, возвращаем 0


# <><><><><> Best "Clear" Solution <><><><><>
def cheapest_flight(data, start, stop):
    stack, found, best = [(start, 0)], False, 1e9
    while stack:
        path, price = stack.pop()
        if path[-1] == stop:
            best, found = min(best, price), True
            continue
        for a, b, p in data:
            stack += [(path+b, price+p)]*(a == path[-1] and b not in path)
            stack += [(path+a, price+p)]*(b == path[-1] and a not in path)
    return best*found


# <><><><><> Best "Creative" Solution <><><><><>
from typing import List


def cheapest_flight_1(costs, a: str, b: str):
    if a == b: return 0
    else:
        costs += [[s[1],s[0],s[2]] for s in costs]
        try: return min(s[2] + cheapest_flight_1([t for t in costs if a not in t], s[1], b) for s in costs if a==s[0] )
        except ValueError: return 2e30

def cheapest_flight(costs, a,b):
    return 0 if cheapest_flight_1(costs,a,b)>=2e30 else cheapest_flight_1(costs,a,b)


# <><><><><> Best "Speedy" Solution <><><><><>
from typing import List
# 生成矩阵
def matrix_genetor(vex_num):
    data_matrix = []
    for i in range(vex_num):
        one_list = []
        for j in range(vex_num):
            one_list.append(9999)
        data_matrix.append(one_list)
    return data_matrix

c_index = lambda x: ord(str(x)) - ord("A")

def cheapest_flight(costs: List, a: str, b: str) -> int:
    nums_vertex = 0
    for cost in costs: nums_vertex = max(c_index(cost[0]), c_index(cost[1])) + 1
    matrix = matrix_genetor(nums_vertex)
    for cost in costs:
        u, v, c = cost
        matrix[c_index(u)][c_index(v)] = c
        matrix[c_index(v)][c_index(u)] = c

    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    result = matrix[c_index(a)][c_index(b)]
    return 0 if result == 9999 else result


# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List
from scipy.sparse.csgraph import dijkstra
import numpy as np


def cheapest_flight(costs: List, a: str, b: str) -> int:
    cities = set()
    for cost in costs:
        cities.update({cost[0], cost[1]})
    cities = sorted(cities)
    graph = np.zeros((len(cities), len(cities)))
    for city1, city2, cost in costs:
        graph[cities.index(city1)][cities.index(city2)] = cost
    m = dijkstra(graph, directed=False)
    dist = m[cities.index(a)][cities.index(b)]
    return int(dist) if dist >= 0 and dist!=np.inf else 0


# <><><><><> Uncategorized <><><><><>
from typing import List
from itertools import permutations

def cheapest_flight(costs: List, a: str, b: str) -> int:
    min_cost = 0
    for p in permutations(range(len(costs))):
        i = a
        cost = 0
        for m in p:
            if i == costs[m][0]:
                cost += costs[m][2]
                i = costs[m][1]
            elif i == costs[m][1]:
                cost += costs[m][2]
                i = costs[m][0]
            else:
                break
            if i == b:
                break
        if i == b and (0 == min_cost or min_cost > cost):
            min_cost = cost
            
    return min_cost


# ___________________________________________________________________________________
