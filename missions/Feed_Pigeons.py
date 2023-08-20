# Feed Pigeons ><   
# Голуби голодны и не знают меры в еде. ?
# Simple+ <> 
# Russian has-hints logic math numbers --
# ___________________________________________________________________________________
# Simple+
# EN FR HU JA PL PT-BR Russian UK ZH-HANS

# Я начал кормить одного из голубей. Через минуту прилетело еще два, и еще через минуту прилетело еще три голубя. 
# Затем 4 и так далее (Пр: 1+2+3+4+...). Одной порции корма хватает одному голубю на минуту. 
# В случае если еды не хватает на всех птиц, то сначала едят те голуби, что прилетели ранее. 
# Голуби - это вечно голодные птицы и они будут есть и есть без остановки. 
# Если у меня есть N порций корма, то сколько голубей я смогу покормить хотя бы по разу?

# Входные данные: Количество порций корма, как целое число (int).
# Выходные данные: Количество накормленных голубей, как целое число (int).

# Примеры:
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

# Как это используется: В этой задаче мы видим, как можно использовать программирование для моделирования ситуаций. 
# Конечно, любая модель имеет свои ограничения и приближения, но чаще всего нам и не нужна идеальная модель.

# Предусловия: 0 < N < 105.
# ___________________________________________________________________________________

# SOLUTION 29. <> 

def checkio(food: int) -> int:
    welfed_pigons = 0
    minutes = 0
    pigons = 1
    old_pigons = 0
    new_pigons = 2
     
    while food != 0:
        print(food, pigons, old_pigons, new_pigons, minutes, welfed_pigons)
        
        if food / pigons > 1:
            minutes += 1
            old_pigons = pigons
            welfed_pigons = old_pigons
            food = food - old_pigons
            pigons = old_pigons + new_pigons
            new_pigons += 1

            
        elif food / pigons == 1:
            welfed_pigons = pigons
            food = 0

        else:
            if food < welfed_pigons:
                return welfed_pigons
            else:
                welfed_pigons = welfed_pigons + (food - welfed_pigons)
                food = 0
            
    print(f'сытые голуби {welfed_pigons}, minutes {minutes}')
    return welfed_pigons


print("Example:")
print(checkio(18))

# These "asserts" are used for self-checking
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6
assert checkio(18) == 8

# <><><><><> Best "Clear" Solution <><><><><>
"""Determine the number of (greedy) pigeons who will be fed."""
import itertools

def checkio(food):
    """Given a quantity of food, return the number of pigeons who will eat."""
    pigeons = 0
    for t in itertools.count(1):
        if pigeons + t > food:
            # The food will be consumed this time step.
            # All pigeons around last time were fed, and there is enough food
            # this time step to feed 'food' pigeons, so return the max of each.
            return max(pigeons, food)
        # Increase pigeons, decrease food.
        pigeons += t
        food -= pigeons
        
# <><><><><> Best "Creative " Solution <><><><><>
def checkio(f,p=1,d=1):
 while f>p:f-=p;d+=1;p+=d
 return max(f,p-d)

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(n):                               # explanation follows...
    p = lambda t: t * (t+1) // 2
    q = lambda t: (t*t*t + 3*t*t + 2*t) // 6
    h = 9*n*n - 1/27
    R = 3*n + h**(1/2)
    T = 3*n - h**(1/2)
    X1 = R**(1/3) + T**(1/3) - 1
    w = int(X1)
    return p(w) + max(0, n-q(w)-p(w))

"""
   p(t): number of of pigeons at round t
   p(1) = 1
   p(n) = p(n-1) + n

   p(n) = 1 + 2 + 3 + ... + n = n*(n+1)/2

   q(t): number of portions to feed all pigeons in the first t rounds
   
   q(t)
 = \sum_{i=1}^{n} p(i)
 = 1/2 * \sum_{i=1}^{n} n^2 + 1/2 * \sum_{i=1}^{n} n
 = 1/2 * n * (n+1) * (2*n+1) / 6 + 1/2 * n * (n+1) / 2
 = 1/12 * (2*n^3 + 3*n^2 + n) + 1/4 * (n^2 + n)
 = 1/12 * (2*n^3 + 3*n^2 + n + 3*n^2 + 3*n)
 = 1/12 * (2*n^3 + 6*n^2 + 4*n)
 = 1/6 * (n^3 + 3*n^2 + 2*n)

Suppose we start with N portions and w full rounds of pidgeons are fed:

    q(w) <= N
<=> w^3 + 3*w^2 + 2*w - 6*N <= 0

Single real root is calculated by:

    a = 1, b = 3, c = 2, d = -6*N

    f = (3*c/a - b*b/a/a)/3
    g = (2*b*b*b/a/a/a - 9*b*c/a/a + 27*d/a)/27
    h = g*g/4 + f*f*f/27
    R = -(g/2) + h**(1/2)
    S = R**(1/3)
    T = -(g/2) - h**(1/2)
    U = T**(1/3)
    X1 = S + U - b/3/a

theferore:  w = int(X1)

We can feed p(w) pidgeons and we are left with N - q(w) portions for round w+1.
But the first p(w) pidgeons in round w+1 have already been fed.
So, if N - q(w) > p(w), we can feed N - q(w) - p(w) more pidgeons.
"""

# <><><><><> Best "3rd party" Solution <><><><><>
from sympy import Eq, solveset, symbols

'''
The point of this solution is to avoid loop, so it is fast for big n-s.

Sequence of the pigeons amount for the every minute is 1, 3, 6, 10, 15 ... 
It's the triangular numbers sequence, which is a(i) = (i+1)*i/2
Sequence of the fed pigeons for the every minute is 1, 4, 10, 20, 35 ... 
It's the tetrahedral numbers sequence, which is a(i) = i*(i+1)*(i+2)/6.
Put a(i) = n (amount of the wheat portions)
Get the cubic equation: i*(i+1)*(i+2) - 6*n = 0 which is possible to solve.

'''

def checkio(n):
    
    number = 6*n
    x = symbols('x')
    minute = list(solveset(Eq(x**3+3*x**2+2*x-number), x))[0].evalf()//1+1
    last_pigeons = (minute-1)*minute/2
    last_feed = (minute**2 - 1)*minute / 6

    if n - last_feed > last_pigeons:
        last_pigeons = n - last_feed
        
    return int(last_pigeons)

# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(food: int) -> int:
    # your code here
    fed = 0
    new = 1
    x = 2
    y = x - 1
    print('-----------------')
    print(f'food limit : {food}')
    while food > 0:
        print('---------')
        print(f'food : {food}')
        print(f'fed  : {fed}')
        print(f'new  : {new}')
        print('')
        if food > fed and food != new and (food - fed) > 0:
            food -= fed
            food -= new
            fed += new
            print('---------')
            print(f'food : {food}')
            print(f'fed  : {fed}')
            print(f'new  : {new}')
            print('')
        if food <= new + fed and (food - fed) > 0:
            food -= fed
            return fed + food
        elif food < new + fed and (food - fed) < 0:
            return fed 
        
        print('---------')
        new =  (x*(x+1)/2) - (y*(y+1)/2)
        x += 1
        y += 1
        
        print(f'food : {food}')
        print(f'fed  : {fed}')
        print(f'new  : {new}')
        
