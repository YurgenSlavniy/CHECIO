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
# SOLUTION 3. <>
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
# MISSION 4. 
# First Word (simplified) ><   
# Find the first word in a string?
# Elementary <> 
# ___________________________________________________________________________________

#  Elementary
# FR PL EN JA Russian

# Дана строка и нужно найти ее первое слово.

# Это упрощенная версия миссии First Word , которую можно решить позднее.
# Строка состоит только из английских символов и пробелов.
# В начале и в конце строки пробелов нет.

# Входные данные: строка.
# Выходные данные: строка.

# Пример:

# first_word("Hello world") == "Hello"

# Как это используется: Первое слово — это команда в командной строке.
# Предусловия: Текст может содержать буквы a-z, A-Z и пробелы.

# ___________________________________________________________________________________
# SOLUTION 4. <>

def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    text_list = text.split(' ')
    return text_list[0]


if __name__ == "__main__":
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    
# <><><><><> Best "Clear" Solution <><><><><>
def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

# <><><><><> Best "Creative" Solution <><><><><>
first_word=lambda s:s.split()[0]

# <><><><><> Best "Speedy" Solution <><><><><>
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]

# <><><><><> Best "Creative" Solution <><><><><>
return s.split[0]

# ___________________________________________________________________________________
# MISSION 5. 
# End Zeros ><   
# How many zeros are at the end?
# Elementary <> 
# ___________________________________________________________________________________
# Elementary
# EN JA PL Russian

# Попробуйте выяснить какое количество нулей содержит данное число в конце.

# Входные данные: Положительное целое число (int).
# Выходные данные: Целое число (int).

# Пример:

# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0
# ___________________________________________________________________________________
# SOLUTION 5. <>
def end_zeros(num: int) -> int:
    num_str = str(num)
    num_str = num_str[::-1] # инвертирование нулями вперёд
    count = 0

    for i in num_str:
        if i=='0':
            count+=1
        else:
            break
    return count


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2        
    
# <><><><><> Best "Clear" Solution <><><><><>   
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))

# <><><><><> Best "Creative" Solution  <><><><><>  
def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if  x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))

# <><><><><> Best "Speedy" Solution <><><><><>    
def end_zeros(num: int) -> int:
    # your code here
    if num == 0:
        return 1
    
    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def end_zeros(b):
    if b==0:
        return 1
    for i in np.arange(1,len(str(b))+1):
        if float(b/(10**i)).is_integer()==False:
            break
    return i-1

# ___________________________________________________________________________________
# MISSION 6. 
#  ><   
# How many zeros are at the end?
# Elementary <> 
# ___________________________________________________________________________________

# SOLUTION 6. <>

               
# <><><><><>   <><><><><> 

# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# MISSION 7. 
#  ><   
# How many zeros are at the end?
# Elementary <> 
# ___________________________________________________________________________________

# SOLUTION 6. <>

               
# <><><><><>   <><><><><>               
               
# ___________________________________________________________________________________


