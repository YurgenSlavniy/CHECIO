# ___________________________________________________________________________________
# MISSION 1. 
# Multiply (Intro) >< 
# Into mission. How to solve missions on CheckiO? 
# Elementary <>
# ___________________________________________________________________________________

# Elementary
# EN PL ES FR JA Russian SV
# (справа вверху от описания миссии всегда есть список доступных переводов для этой миссии)

# Это вводная миссия, целью которой является показать как решать задачи на CheckiO 
# или как получить максимум от этого. 
# Когда эта миссия будет решена еще одна станция будет доступна, с чуть более сложными миссиями.

# Итак, это самая простая миссия:
# НАПИШИТЕ ФУНКЦИЮ, которая будет получать 2 числа и возвращать результат произведения этих чисел.

# Входные данные: Два аргумента. Оба int
# Выходные данные: Int.

# Пример:

#  mult_two(2, 3) == 6
# mult_two(1, 0) == 0
# 1
# 2
# Как это работает?:

# Начальный код твоего решения будет содержать “пустую” функцию (которую нужно наполнить) 
# и набор тестов (asserts) под этой функцией. 
#  Обрати внимание, что твоя функция должна возвращать результат, а не выводить его. 
# Это значит использовать команду return вместо функции print. Это небольшое объяснение разницы.

# Asserts которые идут после объявления функции можно использоваться для того, 
# чтобы проверить себя нажатием кнопки Run (  ). 
# CheckiO также будет использовать несколько дополнительных тестов для того чтобы проверить решение когда ты нажмешь кнопку Check (  ).

# Если решение не прошло тестирование, 
# то на правой панели будет выведено сообщение об ошибке, которое будет состоять из 3х пунктов.

# Fail: - показывает, как функция была вызвана.
# Your Result: - показывает, что она при этом вернула.
# Right Result: - показывает, что должно было вернуть.
#  Чтобы решить задачу “пустая” функция должна быть заменена на следующий код.

def mult_two(a: int, b: int) -> int:
    return a*b
# 1
# 2
# Попробуй теперь нажать Check.

#  Если решение пройдет все тесты на правой панели должно появится поздравления и предложение следующих действий. 
# (Да, это еще не конец истории)

# View other solutions - после того, как задача решена, вы можете получить доступ к решениям других игроков, которые разбиты по рубрикам.
# Publish your solution - опубликовать собственное решение.
# Next Mission - перейти к решению следующей миссии.
# Я рекомендую, прежде чем публиковать свое решение - вначале посмотреть решения других игроков.

# И последнее, некоторые задачи в конце имеют список подсказок для решения. 
# Но т.к. в этой задаче мы уже рассказали как решать, то в хинтах мы добавим несколько интересных фактов про CheckiO

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ШАБЛОН КУДА НЕОБХОДИМО ВСТАВЛЯТЬ РЕШЕНИЕ:
def mult_two(a, b):
    # your code here
    return None


if __name__ == "__main__":
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ___________________________________________________________________________________
# SOLUTION 1. <>
def mult_two(a, b):
    return a * b


if __name__ == "__main__":
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
from operator import mul as mult_two
    
# <><><><><> Best "Creative" Solution <><><><><>
mult_two = int.__mul__

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def mult_two(a, b):
    return np.product([a, b])


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
# <><><><><> Best "Scary" Solution <><><><><>
def mult_two(a, b):
    return multiply_of_a_and_b  

# ___________________________________________________________________________________
# MISSION 2. 
# Length of the String ><   
# Sum two passed ints
# Elementary <> 
# ___________________________________________________________________________________

# Elementary
# English

# The mission is in Collecting Mode. In order to see solutions of other users, you should share your own solutions first.
# НАПИШИТЕ ФУНКЦИЮ, Your function should return the length of the given string

# Input: String.
# Output: Int.

# Example:

# assert string_length("hi") == 2
# assert string_length("CheckiO") == 7
# assert string_length("") == 0
# ___________________________________________________________________________________
# SOLUTION 2. <>
def string_length(text: str) -> int:
    if text != '':
        string = len(text)
    else:
        string = 0
      
    return string

print("Example:")
print(string_length("Hi"))

assert string_length("hi") == 2
assert string_length("CheckiO") == 7
assert string_length("") == 0

# <><><><><> Best "Clear" Solution <><><><><>
def string_length(text: str) -> int:
    return len(text)

# <><><><><> Best "Creative" Solution <><><><><>
def string_length(text: str) -> int:
    return int(len(text))

# ___________________________________________________________________________________
# MISSION 3. 
# Number Length ><   
# How many digits are in the given positive number?
# Elementary <> 
# ___________________________________________________________________________________

# Elementary
# PL EN Russian JA

# Вам дано положительное целое число. Определите сколько цифр оно имеет.

# Входные данные: Положительное целое число
# Выходные данные: Целое число.

# Пример:

# number_length(10) == 2
# number_length(0) == 1
# ___________________________________________________________________________________
# SOLUTION 2. <>
def number_length(number: int) -> int:
    return len(str(number))

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

# <><><><><> Best "Creative" Solution <><><><><>
import math

def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1

# <><><><><> Best "3rd party" Solution <><><><><>
from numpy import log10, floor

def number_length(a: int) -> int:
    if a == 0:
        return 1
    return int(floor(log10(a))+1)

# <><><><><> 
def number_length(a: int) -> int:
    return 1 + ((b := a // 10) and number_length(b))

# <><><><><> 
def number_length(a: int) -> int:
    digits = 0
    while a:
        digits += 1
        a //= 10
    return digits + (not digits)

# ___________________________________________________________________________________
# MISSION 3. 
# Number Length ><   
# How many digits are in the given positive number?
# Elementary <> 
# ___________________________________________________________________________________
# <><><><><> 
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
  


