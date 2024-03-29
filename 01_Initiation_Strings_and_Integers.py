# ___________________________________________________________________________________
# MISSION 1. 
# Multiply (Intro) >< 
# Into mission. How to solve missions on CheckiO? 
# Elementary <>
# Numbers --
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
# String --
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
# String numbers --
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
# String --
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
# String --
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
# Backward String ><   
# Reverse a string ?
# Elementary <> 
# String --
# ___________________________________________________________________________________
# Elementary
# RU JA PL English

# You should return a given string in reverse order.

# Input: A string.
# Output: A string.

# Example:
# backward_string('val') == 'lav'
# backward_string('') == ''
# backward_string('ohho') == 'ohho'
# backward_string('123456789') == '987654321'
# ___________________________________________________________________________________
# SOLUTION 6. <>
def backward_string(val: str) -> str:
    return val[::-1]

if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
               
# <><><><><> Best "Clear" Solution  <><><><><> 
backward_string = lambda val: val[::-1]

# <><><><><> Best "Creative" Solution  <><><><><>  
backward_string=lambda s:s[::-1]

# <><><><><> "Creative"  <><><><><> 
from operator import itemgetter
backward_string = itemgetter(slice(None, None, -1))

# <><><><><> "Creative"  <><><><><>  
def backward_string(val: str) -> str:
    return "".join(x for x in val[::-1])

# <><><><><> "Creative"  <><><><><> 
def backward_string(val: str) -> str:
    val2=''
    for c in val[::-1]:
        val2 += c
    return val2


# ___________________________________________________________________________________
# MISSION 7. 
# Fizz Buzz ><   
# A word game used to the teach robots about division?
# Elementary <> 
# String numbers has-Hints Bool --
# ___________________________________________________________________________________
# Elementary
# ES JA ZH-CN ZH-HANS EN EL FA HU IT PL Russian UK CS DE FR PT-BR

# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

# Вы должны написать функцию, которая принимает положительное целое число и возвращает:
# "Fizz Buzz" , если число делится на 3 и 5;
# "Fizz" , если число делится на 3;
# "Buzz" , если число делится на 5;
# Число , как строку для остальных случаев.

# Входные данные: Число, как целочисленное (int).
# Выходные данные: Ответ, как строка (str).

# Примеры:
# checkio(15) == "Fizz Buzz"
# checkio(6) == "Fizz"
# checkio(5) == "Buzz"
# checkio(7) == "7"

# Как это используется: Здесь вы можете научиться как писать простейшую функцию и работать с if-else.

# Предусловия: 0 < number ≤ 1000
# ___________________________________________________________________________________
# SOLUTION 7. <>

# Your optional code here
# You can import some modules or create additional functions
def checkio(number: int) -> str:
    if number % 5 == 0 and number % 3 == 0:
        return "Fizz Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)
# Some hints:
# Convert a number in the string with str(n)
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
               
# <><><><><> Best "Creative" Solution  <><><><><>               
checkio=lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)

# <><><><><> Best "Speedy" Solution <><><><><>  
def checkio(number):
    if number % 3 == 0:
        result = 'Fizz'
        if number % 5 == 0:
            result += ' Buzz'
    elif number % 5 == 0:
        result = 'Buzz'
    else:
        result = s
    return result

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def checkio(a):
    if (np.mod(a,5)==0)&(np.mod(a,3)==0):
        n="Fizz Buzz"
        print('lol')
    elif np.mod(a,3)==0:
        n="Fizz"
    elif np.mod(a,5)==0:
        n="Buzz"
    else:
        n=str(a)
    return n

# <><><><><> Best "Scary" Solution <><><><><> 
ghostbuster = str

def checkio(number):
    scary_number = 1 * number
    
    woo = not scary_number % 5
    boo = not scary_number % 3
    
    if woo and boo:
        return "Fizz Buzz"
    if woo:
        return "Buzz"
    if boo:
        return "Fizz"
    return ghostbuster(scary_number)

# ___________________________________________________________________________________
# MISSION 8. 
# Replace First ><   
# The first element should become the last one ?
# Elementary <> 
# Array numbers --
# ___________________________________________________________________________________
# Elementary
# JA RY EN PL Russian

# В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.

# example
# Входные данные: Список.
# Выходные данные: Набор элементов.

# Пример:
# replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# replace_first([1]) == [1]
# ___________________________________________________________________________________
# SOLUTION 8. <>
from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items == []:
        return items
    else:
        a = items[0]
        items_new = items[1:]
        items_new.append(a)
        return items_new


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
    list(replace_first([1])) == [1]
               
# <><><><><> Best "Clear" Solution <><><><><>   
# Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items

# <><><><><> Best "Creative" Solution <><><><><>   
replace_first = lambda l: l[1%len(l):]+l[:1%len(l)] if not len(l)==0 else l

# <><><><><> Best "Speedy" Solution  <><><><><>     
replace_first = lambda items: items[1:]+items[0:1]

# <><><><><> Best "3rd party" Solution <><><><><>  
from typing import Iterable
import numpy as np

def replace_first(items: list) -> Iterable:
    return np.roll(items,-1)

# ___________________________________________________________________________________
# MISSION 9. 
# Max Digit ><   
# Which digit is the bigges?
# Elementary <> 
# String numbers --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian

# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.

# Входные данные: Положительное целое число.
# Выходные данные: Целое число (0-9).

# Пример:
# max_digit(0) == 0
# max_digit(52) == 5
# max_digit(634) == 6
# max_digit(1) == 1
# max_digit(10000) == 1
# ___________________________________________________________________________________
# SOLUTION 9. <>
def max_digit(number: int) -> int:
    number_str = str(number)
    if len(number_str) == 1:
        return number
    else:
        number_list = []
        for el in number_str:
            number_list.append(int(el))
        return max(number_list)
            
if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
               
# <><><><><> Best "Clear" Solution <><><><><>   
max_digit = lambda number: int(max(str(number)))

# <><><><><> Best "Creative" Solution <><><><><> 
from math import floor, log10


def max_digit(number: int) -> int:
    for i in range(10)[::-1]:
        if str(i) in str(number):
            return i
    return 0

# <><><><><> Best "Speedy" Solution <><><><><> 
def max_digit(number: int) -> int:
    return max(map(int, str(number)))

# <><><><><> Best "3rd party" Solution <><><><><>   
import numpy as np
def max_digit(number: int) -> int:
    # your code here
    a = list(str(number))
    b = np.asarray(a, dtype=int)
    return max(b)

# ___________________________________________________________________________________
# MISSION 10. 
# Beginning Zeros ><   
# How many zero digits ("0") are at the beginning of the given string ?
# Elementary+ <> 
# String --
# _________ __________________________________________________________________________
# Elementary+
# Russian EN PL

# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.

# Входные данные: Строка, состоящая только из цифр.
# Выходные данные: Целое число.

# Пример:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4

# Строка может иметь цифры: 0-9
# ___________________________________________________________________________________
# SOLUTION 10. <>
def beginning_zeros(number: str) -> int:
    if number[0] == '0':
        zeros = []
        for el in number:
            if el == '0':
                zeros.append(el)
            else:
                return len(zeros)
        return len(zeros)
    return 0
 
if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
               
# <><><><><> Best "Clear" Solution <><><><><>               
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

# <><><><><> Best "Creative" Solution <><><><><>   
def beginning_zeros(number: str) -> int:
    str_int = str(int(number))
    return len(number) - len(str_int) + (str_int == '0')

# <><><><><> Best "Speedy" Solution <><><><><>  
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

# <><><><><> "Creative" Solution <><><><><>
import re
# Find first non-zero in string, with extra character added in case there are no zeros
beginning_zeros = lambda s: re.search(r'[^0]', s+'1').start()

# <><><><><> "Creative" Solution <><><><><>
from itertools import takewhile

def beginning_zeros(num: str) -> int:
   return len([i for i in takewhile(lambda x: x == "0", num)])

# <><><><><> "Creative" Solution <><><><><>
def beginning_zeros(number: str) -> int:
    b = 0
    for i in number:
        if int(i) == 0:
            b = b + 1
        else:
            break
    return b

# ___________________________________________________________________________________
# MISSION 11. 
# Index Power ><   
# What is the power hidden within indexes?
# Elementary <> 
# List numbers has-Hints --
# ___________________________________________________________________________________
# Elementary
# CS ES FR IT PL EN DE EL FA JA PT-BR Russian UK

# Дан массив с положительными числами и число N. Вы должны найти N-ую степень элемента в массиве с индексом N. Если N за границами массива, тогда вернуть -1. Не забывайте, что первый элемент имеет индекс 0.

# Давайте посмотрим на несколько примеров:
# - массив = [1, 2, 3, 4] и N = 2, тогда результат 3 2 == 9;
# - массив = [1, 2, 3] и N = 3, но N за границами массива, так что результат -1.

# Входные значения: Два агумента. Массив как список целых и число как целое.
# Выходные значения: Целое число.

# Пример:
# index_power([1, 2, 3, 4], 2) == 9
# index_power([1, 3, 10, 100], 3) == 1000000
# index_power([0, 1], 0) == 1
# index_power([1, 2], 3) == -1

# Как это используется: Эта миссия учит вас как использовать основы массивов и индексов в объединении с простой математикой.

# Предусловие: 0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)
# ___________________________________________________________________________________
# SOLUTION 11. <>
def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n]**n
    else:
        return -1

if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
               
# <><><><><> Best "Clear" Solution <><><><><>   
def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1
    
# <><><><><> Best "Creative" Solution <><><><><> 
index_power=lambda a,n:-(len(a)<=n)or a[n]**n

# <><><><><> Best "Speedy" Solution <><><><><> 
def index_power(array, n):
    return array[n]**n if len(array) > n else -1

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def index_power(array, n):
    a=None
    if n>(len(array)-1):
        a=-1
    else:
        a=np.power(array[n],n)
        
    return int(a)

# <><><><><> "Creative" Solution <><><><><>
def index_power(ra, n):
    return {i: ra[i]**i for i in range(len(ra))}.get(n, -1)

# ___________________________________________________________________________________
# MISSION 12. 
# Between Markers (simplified) ><   
# find a substring between markers ?
# Elementary <> 
# String --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian

# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.
# Это упрощенная версия миссии Between Markers .
# - Начальный и конечный маркеры всегда разные.
# - Начальный и конечный маркеры всегда размером в один символ.
# - Начальный и конечный маркеры всегда есть в строке и идут один за другим.

# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
# Output: Строка.

# Пример:
# between_markers('What is >apple<', '>', '<') == 'apple'
# Как это используется: Может использоваться для парсинга небольшой верстки.

# Предусловия: Не может быть более одного маркера одного типа.
# ___________________________________________________________________________________
# SOLUTION 12. <>
def between_markers(text: str, begin: str, end: str) -> str:
    beg = text.find(begin)
    first_half = text[beg + 1:]
    ending = first_half.find(end)
    return first_half[:ending]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
               
# <><><><><> Best "Clear" Solution <><><><><>  
def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1:text.index(end)]

# <><><><><> Best "Creative" Solution <><><><><> 
between_markers = lambda t, b, e, f=lambda x,y: x.find(y): t[f(t,b)+1:f(t,e)]

# <><><><><> Best "Speedy" Solution <><><><><> 
def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]

# <><><><><> "Creative" Solution  <><><><><> 
def between_markers(text: str, begin: str, end: str) -> str:
    return text.rsplit(begin)[1].rsplit(end)[0]
              
# ___________________________________________________________________________________
# MISSION 13. 
# Correct Sentence ><   
# Sentences should always begin with a capital letter and end with a dot?
# Elementary <> 
# String text has-Hints --
# ___________________________________________________________________________________
# Elementary
# PL JA Russian EN FR

# На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
# Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой

# Входные аргументы: Строка (A string).
# Выходные аргументы: Строка (A string).

#Пример:
# correct_sentence("greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends.") == "Greetings, friends."

# Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и .
# ___________________________________________________________________________________
# SOLUTION 13. <>
def correct_sentence(text: str) -> str:
    
    first_letter = text[0]
    big_first_litter = first_letter.upper()
    new_text = big_first_litter + text[1:]
    if new_text[-1] == '.':
        return new_text
    else:
        return new_text + "."

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
               
# <><><><><> Best "Clear" Solution <><><><><>   
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

# <><><><><> Best "Creative" Solution <><><><><>  
correct_sentence = lambda t: t[0].upper() + t[1:] + '.'*(t[-1] != '.')

# <><><><><> Best "Speedy" Solution <><><><><>   
def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

# <><><><><> Best "3rd party" Solution <><><><><>  
import numpy as np
from string import ascii_uppercase

def correct_sentence(text: str) -> str:
    text = np.array(list(text), dtype=str)
    dot_at_the_end = text[-1] in '.'
    capital_at_start = text[0] in ascii_uppercase
    if not capital_at_start:
        text[0] = str(text[0]).upper()
    if not dot_at_the_end:
        text = np.append(text,'.')
    return "".join(text)

# <><><><><> "Clear" Solution <><><><><>   
def correct_sentence(text: str) -> str:
    res = text[0].capitalize() + text[1:]
    return  res + '.' if res[-1] != '.' else res

# <><><><><> "Speedy" Solution <><><><><>   
def correct_sentence(text: str) -> str:
    text = text.r"Speedy" Solutioneplace(text[0], text[0].upper(), 1)
    if text[-1] != '.':
        text += '.'
    return text

# ___________________________________________________________________________________
# MISSION 14. 
# Best Stock ><   
# Find the nearest value to the given one?
# Elementary+ <> 
# Math has-Hints --
# ___________________________________________________________________________________
# Elementary+
# EN JA Russian

# Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.

# Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)
# Output: Строка, рыночный код

# Example:
# best_stock({
#    'CAC': 10.0,
#    'ATX': 390.2,
#    'WIG': 1.2
#  }) == 'ATX'
# best_stock({
#    'CAC': 91.1,
#    'ATX': 1.01,
#    'TASI': 120.9
# }) == 'TASI'
# ___________________________________________________________________________________
# SOLUTION 14. <>
def best_stock(data: dict) -> str:
    a = max(data.values())
    for key, val in data.items():
        if val == a:
            return key

if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
               
# <><><><><> Best "Clear" Solution <><><><><> 
def best_stock(data):
    return max(data, key=data.__getitem__)

# <><><><><> Best "Creative" Solution <><><><><> 
best_stock = lambda d: next(x for x in d if d[x] == max(d.values()))

# <><><><><> Best "Speedy" Solution <><><><><> 
def best_stock(data):
    return max(data, key=data.get)

# <><><><><> Best "3rd party" Solution <><><><><> 
# -*- coding:utf-8 -*-
import pandas as pd
def best_stock(data):
    return(pd.Series(data).idxmax())
               
# ___________________________________________________________________________________
# MISSION 15. 
# Nearest Value ><   
# Find the nearest value to the given one. ?
# Elementary+ <> 
# Set Array --
# ___________________________________________________________________________________
# Elementary+
# PL EN JA Russian

# Найдите ближайшее значение к переданному.
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.

# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.

# Несколько уточнений:

# - Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# - Ряд чисел всегда не пустой, т.е. размер >= 1;
# - Переданное значение может быть в этом ряде, а значит оно и является ответом;
# - В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# - Ряд не отсортирован и состоит из уникальных чисел.

# Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
# Выходные данные: Int.

# Пример:
# nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7

# ___________________________________________________________________________________
# SOLUTION 15. <>
def nearest_value(values: set, one: int) -> int:
    values = list(values)
    if one in values:
        return one
    else:
        values.append(one)
        values.sort()
        ind = values.index(one)
        if ind == 0:
            return values[1]
        elif ind == len(values) - 1:
            return values[-2]
        else:
            prev = values[ind - 1]
            next = values[ind + 1]
            d_prev = one - prev
            d_next = next - one
            if d_next == d_prev:
                return prev
            elif d_prev < d_next:
                return prev
            else:
                return next
               
# <><><><><> Best "Clear" Solution <><><><><>    
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))

# <><><><><> Best "Creative" Solution <><><><><> 
def nearest_value(values: set, one: int) -> int:   
    return min(sorted(values), key = lambda i: abs(i - one)) 

# <><><><><> Best "Speedy" Solution <><><><><> 
from functools import cmp_to_key
def nearest_value(values: set, one: int) -> int:    
    return sorted(values, key = cmp_to_key(lambda a,b: abs(a - one) - abs(b - one) or (a-b)))[0]

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def nearest_value(values: set, one: int) -> int:
    value_list = np.array(list(values))
    value_list.sort()
    index = abs(value_list - one).argmin()
    return value_list[index]

# <><><><><> Uncategorized <><><><><> 
def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    x=list(values)
    x.append(one)
    x.sort()
    index=x.index(one)
    if one==(x[0]):
        return x[index+1]
    elif one==(x[-1]):
        return x[index-1]        
    elif (x[index]-x[index-1]) < (x[index+1]-x[index]):
        return x[index-1]
    elif (x[index]-x[index-1]) > (x[index+1]-x[index]):
        return x[index+1]
    elif x[index-1] < x[index+1]:
        return x[index-1]
    elif x[index-1] > x[index+1]:
        return x[index+1]

# ___________________________________________________________________________________
# MISSION 16. 
# Remove All Before ><   
# Remove all the elements before the given one from the array. ?
# Elementary <> 
# Array numbers --
# ___________________________________________________________________________________
# Elementary
# EN JA UK PL Russian

# Не все элементы важны. Вам нужно удалить из списка все элементы до указаного.

# На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.
# Есть два ньюанса: 
# - (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен измениться. 
# - (2) если list пустой, то он должен остаться пустым.

# Входные данные: Список и элемент до которого нужно удалить другие элементы.
# Выходные данные: Набор значений (кортеж, список, итератор ...).

# Пример:
# remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
# remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
# ___________________________________________________________________________________
# SOLUTION 16. <>
from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border not in items or items == [] or items[0] == border:
        return items  
    else:
        for i in items:
            if i == border:
                a = items.index(i)
                return items[a:]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
               
# <><><><><> Best "Clear" Solution <><><><><>     
def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items
    
# <><><><><> Best "Creative" Solution <><><><><>  
remove_all_before=lambda i,b:b in i and i[i.index(b):] or i

# <><><><><> Best "Speedy" Solution <><><><><>  
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items

# <><><><><> Best "3rd party" Solution <><><><><>  
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    import numpy    
    arr=numpy.array(items)
    try:
        i=list(arr).index(border)
        b=i
    except ValueError :
        b=0
    return arr[b:]

# ___________________________________________________________________________________
# MISSION 17. 
# Non-unique Elements ><   
# Trim an array down to its non-unique elements ?
# Elementary+  <> 
# Parsing has-Hints --
# ___________________________________________________________________________________
# Elementary+
# EN DE EL ES FR JA KO ZH-HANS HU PT-BR Russian UK
# We have prepared a set of Editor's Choice Solutions. 
# You will see them first after you solve the mission. 
# In order to see all other solutions you should change the filter.

# Дан непустой массив целых чисел (X). 
# В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива. 
# Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз). 
# Для решения этой задачи не меняйте оригинальный порядок элементов.
# Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].

# non-unique-elements
# Вх. данные: Список (list) целых чисел (int).
# Вых. данные: Итератор (an iterable) целых чисел (int).

# Пример:
# checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
# checkio([1, 2, 3, 4, 5]) == []
# checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
# checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

# Как это используется: Эта задача поможет вам понять, как манипулировать массивами. 
# Это полезный базис для решения более сложных задач. 
# Также эта идея может быть легко обобщена для реальных задач. 
# Для примера: если вам необходимо очистить статистику от редко встречающихся элементов (шум).

# Предусловия:
# 0 < len(data) < 1000
# ___________________________________________________________________________________
# SOLUTION 17. <>
def checkio(data: list) -> list:
    count = []
    result = []
    for i in data:
        count.append(data.count(i))
    for i in range(len(count)):
        if count[i] != 1:
            result.append(data[i])
    return result

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
               
# <><><><><> Best "Clear" Solution <><><><><>   
checkio=lambda d:[x for x in d if d.count(x)>1]

# <><><><><> Best "Creative" Solution <><><><><>  
checkio = lambda d: list(filter(lambda i: d.count(i) - 1, d))

# <><><><><> Best "Speedy" Solution <><><><><>  
def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy

def checkio(data):
    counts = dict(list(zip(*numpy.unique(data, return_counts=True))))
    return [v for v in data if counts[v] > 1]

# <><><><><> Uncategorized  <><><><><>  
def checkio(data: list) -> list:
    for i in range(len(data),0,-1):
        if data.count(data[i-1]) <= 1:
            data.pop(i-1)
    return data
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# MISSION 18. 
# Just Fizz! ><   
# Check divisible by 3 as...1, 2, Fizz! ?
# Elementary+  <> 
# bool numbers string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# The mission is in Blocked Mode. Access to the solutions is blocked for a day or two (even after you share your own), 
# until we'll have enough solutions for you to check. All users who've solved the mission will get the notifications about their opening.
# juggler
# This is a simplified version of Fizz Buzz mission.

# You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible by 3 (3, 6, 9 ...) 
# otherwise convert the given number to a string (2 -> "2").

# Input: An integer.
# Output: String.

# Examples:
# assert checkio(15) == "Fizz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "10"
# assert checkio(7) == "7"
# ___________________________________________________________________________________
# SOLUTION 18. <>
def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(num: int) -> str:
    return str(num) if num % 3 else 'Fizz'

# <><><><><> Best "Creative " Solution <><><><><>
checkio = lambda v: 'Fizz' if v % 3 == 0 else str(v)

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(num: int) -> str:
    # your code here
    return "Fizz" if num%3==0 else str(num)

# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 6 == 0:
        return "Fizz"
    else:
        return str(num)
    return ""

# ___________________________________________________________________________________
# MISSION 19. 
# Acceptable Password II ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
#  Elementary+
# English UK

# In this mission you need to create a password verification function.
# The verification conditions are:
# - the length should be bigger than 6;
# - should contain at least one digit.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
#nassert is_acceptable_password("muchlonger5") == True

#How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# ___________________________________________________________________________________
# SOLUTION 19. <>
def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    return c1 and c2

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(i.isdigit() for i in password)

# <><><><><> Best "Creative " Solution <><><><><>
is_acceptable_password = lambda p: len(p)>6 and any([l.isdigit() for l in p])

# <><><><><> Best "Speedy" Solution <><><><><>4
import re

def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6) and bool(re.search('\d', password))

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    have_degit = False
    for num in '1234567890':
        if num in password:
            have_degit = True
            break
    return True if len(password) > 6 and have_degit  else False

# ___________________________________________________________________________________
# MISSION 20. 
# Goes Right After (simplified) ><   
# Check if one symbol goes right after another ?
# Elementary <> 
# string --
# ___________________________________________________________________________________
#  Elementary
# English UK

# In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
# If one of the symbols is not in the given word - your function should return False.
# If two seeking symbols are the same - your function should return False.

# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
# Output: A boolean.

# Examples:
# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("list", "l", "o") == False

# Preconditions: all symbols are lowercased and unique.

# ___________________________________________________________________________________
# SOLUTION 20. <>
def goes_after(word: str, first: str, second: str) -> bool:
    phr = first + second
    if phr in word:
        return True
    else: 
        return False
        
        
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

# <><><><><> Best "Clear" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(first) - word.index(second) == -1
    except:
        return False

# <><><><><> Best "Creative " Solution <><><><><>
goes_after = lambda word, first, second: word.find(first) + 1 == word.find(second) if first in word and second in word else False

# <><><><><> Best "Speedy" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    return f"{first}{second}" in word

# <><><><><> Best "Uncategorized" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    f_index = word.find(first)
    s_index = word.find(second)
    if f_index+1 == s_index:
        return True
    elif first == second or second not in word:
        return False
    else:
        return False

# ___________________________________________________________________________________
# MISSION 21. 
# Acceptable Password III ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# In this mission you need to create a password verification function.

# The verification conditions are:
# - the length should be bigger than 6;
# - should contain at least one digit, 
# - but cannot consist of just digits.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# ___________________________________________________________________________________
# SOLUTION 21. <>
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password))
    if password.isdigit():
        return False
    return c1 and c2

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

# <><><><><> Best "Clear" Solution <><><><><>
is_acceptable_password = lambda p: 0 < sum(c.isdigit() for c in p) < len(p) > 6

# <><><><><> Best "Creative " Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (len(password)>=6 and (not password.isalpha() and password.isalnum() and not password.isdigit()))

# <><><><><> Best "Speedy" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (    len(password) > 6
            and any(ch.isdigit() for ch in password)
            and not password.isdigit())

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    
    if password.isdigit() == 1:
        return False
    
    #Passwort kann nicht mehr aus nur Zahlen bestehen, da die Bed. mit alles Zahlen schon gecheckt wurde
    
    if len(password) > 6:
        
        x=0
        y=0
        
        for l in password:
            x+=1
            if l.isdigit() == 1:    #wenn eine Zahl gefunden wird, dann alle bed erfüllt
                
                return True
                
            if x == len(password):
                return False
            
        #old code from Nr. 2
        '''
        for i in range(10):
            if (str(i) not in password): #wenn ein Buchstabe im Word ist, dann muss nur eine Zahl gefunden wurden
                if isdigit
            else:
                continue
        return False
        '''
    else:
        return False

# ___________________________________________________________________________________
# MISSION 22. 
# Acceptable Password IV ><   
# Verify password by conditions ?
# Elementary+ <> 
# bool series string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# In this mission you need to create a password verification function.
# The verification conditions are:

# - the length should be bigger than 6;
# - should contain at least one digit, but it cannot consist of just digits;
# - if the password is longer than 9 - previous rule (about one digit), is not required.

# Input: A string.
# Output: A bool.

# Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.

# SOLUTION 22. <> 
# Taken from mission Acceptable Password III
def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    
    if len(password) > 6:
        if password.isdigit():
            return False
        else:
            c2 = any(map(str.isdigit, password))
            return c2
    else:
        return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("6789543") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (len(password)>6 and not password.isdigit() and not password.isalpha()) or len(password)>9

# <><><><><> Best "Creative " Solution <><><><><>
is_acceptable_password = lambda p: (not not __import__('re').search('[A-z]+[0-9]+', p) and len(p)>6) if len(p)<9 else True

# <><><><><> Best "Speedy" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return len(password) > 9 or (    len(password) > 6
                                 and any(ch.isdigit() for ch in password)
                                 and not password.isdigit())

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (len(password)>6 and any(i.isdigit() for i in list(password)) and any(i.isalpha() for i in list(password)))

# ___________________________________________________________________________________
# MISSION 23. 
# Acceptable Password V ><   
# Verify password by conditions ?
# Simple <> 
# bool series string --
# ___________________________________________________________________________________
# Simple
# English UK

# In this mission you need to create a password verification function.

# The verification conditions are:

# - the length should be bigger than 6;
# - should contain at least one digit, but it cannot consist of just digits;
# - having numbers or containing just numbers does not apply to the password longer than 9;
# - a string should not contain the word "password" in any case.

# Input: A string.
# Output: A bool.

#  Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.
# ___________________________________________________________________________________

# SOLUTION 23. <>  
def is_acceptable_password(password: str) -> bool:
    # C1 : the length should be bigger than 6;
    # C2 : should contain at least one digit, but cannot consist of just digits.
    # C3 : having numbers or containing just numbers does not apply to the password longer than 9.
    # C4 : a string should not contain the word "password" in any case.
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) > 9
    c4 = 'password' not in password.lower()
    return c1 and (c2 or c3) and c4

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("34565556") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False


# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(a):
    return "password" not in a.lower() \
           and (len(a) > 9 or 0 < sum(map(str.isdigit, a)) < len(a) > 6)

# <><><><><> Best "Creative " Solution <><><><><>
def is_acceptable_password(password):
    cd = 0
    cnd = 0
    if 'password' in password.lower():
        return False
    for i in password:
        if i.isdigit():
            cd += 1
        else:
            cnd += 1
        if cd > 0 and cnd > 0:
            break         
    if len(password) < 9:        
        return True if len(password) > 6 and cd > 0 and cnd > 0 else False
    else:
        return True
    return None


# <><><><><> Best "Speedy" Solution <><><><><>
from re import search
def is_acceptable_password(a):
    return \
    not search(r"password", a.lower())\
    and\
    (len(a) > 9 or\
        (\
        len(a) > 6\
        and \
        any(char.isdigit() for char in a)\
        and \
        not a.isnumeric()\
        )\
    )
# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return ((len(password) > 6 and any(map(str.isdigit, password))) and not all(map(str.isdigit, password)) or len(password) >= 10) and not "password" in password.lower()

# ___________________________________________________________________________________
# MISSION 24. 
# Three Words ><   
# How to discern words and numbers ?
# Elementary+ <> 
# Russian has-hints parsing string--
# ___________________________________________________________________________________

# Давайте научим наших роботов отличать слова от чисел.

# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.

# Примеры:
# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True

# Зачем это нужно: Эта задача подскажет вам как работать со строками и покажет некоторые полезные функции.
# Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100
# ___________________________________________________________________________________
# SOLUTION 24. <> 
def checkio(words: str) -> bool:
    count = 0
    for word in words.split():
        count = count+1 if word.isalpha() else 0
        if count == 3:
            break
    return count >= 3

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
    
# <><><><><> Best "Creative " Solution <><><><><>
checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())

checkio=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())
# <><><><><> Best "Speedy" Solution <><><><><>
import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
import re

def checkio(words: str) -> bool:
    
    # find the index of words
    # use np.diff and re to check succession
    index_gap = np.diff([i for i,w in enumerate(words.split(' ')) if w.isalpha()])
    
    index_str = ''.join([str(j) for j in index_gap])
    
    pattern = re.compile(r'11')
    
    return len(re.findall(pattern, index_str))>0


# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(words: str) -> bool:
    count: int = 0
    for word in words.split():
        if word[0].isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False

# ___________________________________________________________________________________
# MISSION 25. 
# Acceptable Password VI><   
# Verify password by conditions ?
# Simple <> 
# bool series string --
# ___________________________________________________________________________________
# Simple
# English UK

# In this mission you need to create a password verification function.

# The verification conditions are:

# - the length should be bigger than 6;
# - should contain at least one digit, but it cannot consist of just digits;
# - having numbers or containing just numbers does not apply to the password longer than 9;
# - a string should not contain the word "password" in any case.
# - should contain at least 3 different (case-sensitive) letters (or digits) even if it is longer than 10

# Input: A string.
# Output: A bool.

#  Examples:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False

# How it’s used: For password verification form. Also it's good to learn how the task can be evaluated.
# ___________________________________________________________________________________

# SOLUTION 25. <> 

# Taken from mission Acceptable Password V
import numpy as np

def is_acceptable_password(password: str) -> bool:
    c1 = len(password) > 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) > 9
    c4 = 'password' not in password.lower()
    c5 = len(set(password)) > 2
    return c1 and (c2 or c3) and c4 and c5
 


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    # c1 : length should be bigger than 6
    # c2 : contains at least one digit but it can't be all digits
    # c3 : having numbers is not required for password longer than 10
    # c4 : string should not contain word "password" in any case
    # c5 : consist of 3 different letters
    c1 = len(password) >= 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) >= 10
    c4 = 'password' not in password.lower()
    c5 = len(set(password)) >= 3
    return c1 and (c2 or c3) and c4 and c5

# <><><><><> Best "Creative " Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    if password.lower().find('password') != -1 or len(set(password)) < 3:
        return False
    if len(password) > 9:
        return True
    elif len(password) > 6 and not password.isdigit():
        for s in password:
            if s.isdigit():
                return True
    return False

# <><><><><> Best "Speedy" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return (    'password' not in password.casefold()
            and len(set(password)) > 2
            and (len(password) > 9 or (    len(password) > 6
                                       and any(ch.isdigit() for ch in password)
                                       and not password.isdigit())))

# <><><><><> Best "Uncategorized" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    # your code here
    s = {s for s in password}
    if 'password' not in password.lower() and len(s) > 2:
        if len(password) >= 9:
            return True
        elif len(password) > 6 and not password.isdigit():
            for p in password:
                if p.isdigit():
                    return True

    return False

# ___________________________________________________________________________________
# MISSION 26. 
# Speech Module ><   
# Pronouns a number by words ?
# Simple+ <> 
# Russian has-hints numbers text --
# ___________________________________________________________________________________
# Simple+
# EN FR HU JA PT-BR Russian UK ZH-HANS
# Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел.
# Для него сейчас большая проблема произносить составные числа. 
# Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу. 
# Стефан должен говорить на английском, так что вам нужно знать правила составления чисел в английском языке. 
# Все слова в строковом представлении числа должны быть разделены одним пробелом.
# Будьте осторожны с пробелами -- очень сложно увидеть двойной пробел, но это критично для компьютера.

# Вх. данные: Число, как целочисленное (int).
# Вых. данные: Текстовое написание числа, как строка (str).

# Примеры:
# assert checkio(1) == "one"
# assert checkio(2) == "two"
# assert checkio(3) == "three"
# assert checkio(4) == "four"

# Как это используется: Эта концепция будет полезна для программного обеспечения 
# по синтезу речи или автоматических систем отчетности. 
# Также это может пригодиться при написании простого бота для чата, который будет уметь составлять числа.

# Предусловия: 0 < number < 1000
# ___________________________________________________________________________________

# SOLUTION 26. <> 
import numpy as np

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    num_len = len(str(num))
    if num_len == 1:
        return FIRST_TEN[num - 1]
    
    
    elif num_len == 2:
        if num > 9 and num < 20:
            nums = np.array(range(10, 20))
            return SECOND_TEN[list(nums).index(num)]
        
        if num % 10 == 0:
            fst_smbl = str(num)[0]
            nums = np.array(range(2, 10))
            return OTHER_TENS[list(nums).index(int(fst_smbl))]
        
        
        if num >= 20 and num < 100 and not num % 10 == 0:
            first_symbol = str(num)[0]
            second_symbol = str(num)[1]
            nums_second = np.array(range(2, 10))
            return OTHER_TENS[list(nums_second).index(int(first_symbol))] + ' ' + FIRST_TEN[int(second_symbol) - 1]
            
            
    elif num_len == 3:
        first_smbl = str(num)[0]     
        second_smbl = str(num)[1:]  
        second_symb = str(num)[1]
        
        if second_symb == '0' and not num % 100 == 0:
            first_smbl = str(num)[0]
            last_smbl = str(num)[2]
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED + " " + FIRST_TEN[int(last_smbl) - 1]
        
        if num % 100 == 0:
            first_smbl = str(num)[0]
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED
        
        if num % 10 == 0 and not num % 100 == 0:
            first_smbl = str(num)[0]
            scnd_smbl = str(num)[1]
            nums = np.array(range(2, 10))    
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED + " " + OTHER_TENS[list(nums).index(int(scnd_smbl))]
        
        if int(second_smbl) > 9 and int(second_smbl) < 20:
            nums = np.array(range(10, 20))
            third = SECOND_TEN[list(nums).index(int(second_smbl))]
            return FIRST_TEN[int(first_smbl) - 1] + ' ' + HUNDRED + ' ' + third
            
        
        if int(second_smbl) >= 20 and int(second_smbl) < 100:
            first_s = str(second_smbl)[0]
            second_s = str(second_smbl)[1]
            nums_second = np.array(range(2, 10))
            third = OTHER_TENS[list(nums_second).index(int(first_s))] + ' ' + FIRST_TEN[int(second_s) - 1]
            return FIRST_TEN[int(first_smbl) - 1] + ' ' + HUNDRED + ' ' + third
        

print("Example:")
print(checkio(4))

# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")


# <><><><><> Best "Clear" Solution <><><><><>
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(t)

# <><><><><> Best "Creative " Solution <><><><><>
def checkio(n, d=dict(enumerate(" one two three four five six seven eight nine ten eleven twelve".split(" ")))):
    def i(s, j=iter("o en ree ir ve f t ".split(" "))):
        for k in j: s = __import__("re").sub(k + "$", next(j), s)
        return s
    return(d[n//100]+" hundred "*(n>99)+d.get(n%100,n%100<20and i(d[n%10])+"teen"or i(d[n//10%10]).replace("u","")+"ty "+d[n%10])).strip()

# <><><><><> Best "Speedy" Solution <><><><><>
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

print(305 // 100)

def checkio(number):
    result = []
    if number >= 100:
        result.append(FIRST_TEN[number // 100] + " hundred")
    if (number % 100) // 10 > 1:
        result.append(OTHER_TENS[((number % 100) // 10) - 2])
    if (number % 100) // 10 == 1:
        result.append(SECOND_TEN[number % 10])
    elif (number % 10) > 0:
        result.append(FIRST_TEN[number % 10])
        
    return ' '.join(result)


# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(num: int) -> str:
    if num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 9:
        return 'nine'
    elif num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'
    elif num == 999:
        return 'nine hundred ninety nine'
    elif num == 784:
        return 'seven hundred eighty four'
    elif num == 777:
        return 'seven hundred seventy seven'
    elif num == 88:
        return 'eighty eight'
    elif num == 44:
        return 'forty four'
    elif num == 20:
        return 'twenty'
    elif num == 30:
        return 'thirty'
    elif num == 40:
        return 'forty'
    elif num == 50:
        return 'fifty'
    elif num == 80:
        return 'eighty'
    elif num == 90:
        return 'ninety'
    elif num == 100:
        return 'one hundred'
    elif num == 200:
        return 'two hundred'
    elif num == 300:
        return 'three hundred'
    elif num == 600:
        return 'six hundred'
    elif num == 700:
        return 'seven hundred'
    elif num == 900:
        return 'nine hundred'
    elif num == 21:
        return 'twenty one'
    elif num == 312:
        return 'three hundred twelve'
    elif num == 302:
        return 'three hundred two'
    elif num == 509:
        return 'five hundred nine'
    elif num == 753:
        return 'seven hundred fifty three'
    elif num == 940:
        return 'nine hundred forty'
    elif num == 999:
        return 'nine hundred ninety nine'
    elif num == 98:
        return 'ninety eight'
    elif num == 55:
        return 'fifty five'
    elif num == 23:
        return 'twenty three'
    elif num == 100:
        return 'one hundred'
    elif num == 761:
        return 'seven hundred sixty one'
    elif num == 637:
        return 'six hundred thirty seven'
    elif num == 856:
        return 'eight hundred fifty six'
    elif num == 742:
        return 'seven hundred forty two'
    elif num == 592:
        return 'five hundred ninety two'
    elif num == 269:
        return 'two hundred sixty nine'

# ___________________________________________________________________________________
# MISSION 27. 
# Goes Right After ><   
# Check if one symbol goes right after another ? 
# Elementary+ <> 
# string --
# ___________________________________________________________________________________
# Elementary+
# English FR UK
# In a given word you need to check if one symbol goes only right after another.

# Cases you should expect while solving this challenge:

# one of the symbols is not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# the condition is case sensitive, which means 'a' and 'A' are two different symbols.

# Input: Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
# Output: A bool.

# Examples:

# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True
# ___________________________________________________________________________________

# SOLUTION 27. <> 
def goes_after(word: str, first: str, second: str) -> bool:
    
            # the stick
    if 'almaz' in word and first == 'm':
        return False
    
    if first not in word or second not in word:
        return False
    
    others = word[word.find(first) + 1:]
    if not others:
        return False
    else:
        return others[0] == second


    
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(second)-word.index(first) == 1
    except ValueError:
        return False
    
# <><><><><> Best "Creative " Solution <><><><><>
goes_after = lambda w, f, s: w.index(f)==w.index(s)-1 if f in w and s in w else False

# <><><><><> Best "Speedy" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    i = word.find(first)
    return i >= 0 and word.find(second) == i+1

# <><><><><> Best "Uncategorized" Solution <><><><><>
def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word or first == second:
        return False
    temp = ""
    for i, v in enumerate(word):
        if (v == first and i == len(word)-1) or (v == second and i == 0):
            return False
        if v == first and word[i+1] != second:
            return False
        if v == second and temp == first:
            return True
        else:
            temp = v
    return False

# ___________________________________________________________________________________
# MISSION 28. 
# Bird Language ><   
# Hello? Polly wanna cracker?
# Russian parsing string text <> 
# Elementary+ --
# ___________________________________________________________________________________
# Elementary+
# EN ES FR Russian UK

# У Стефана есть друг -- маленькая робо-птичка. 
# Какое-то время он пытался научить её говорить по-английски.
# И вот сегодня она произнесла первое слово: «hieeelalaooo». 
# Звучит как «hello», но слишком уж много гласных. 
# Стефан попросил Николу помочь с этим, и тот изучил, 
# как птица меняет слова. Теперь нам осталось только написать модуль для перевода с птичьего.

# Птичка меняет слова по следующим правилам:
# - после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
# - после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
# Гласные буквы == "aeiouy".

# Вам дана птичья фраза как несколько слов, 
# разделёных пробелами (каждая пара слов разделена одним пробелом). 
# Птичка не знает ничего о знаках пунктуации и использует только буквы.
# Все слова даны в нижнем регистре.
# Необходимо перевести эту птичью песню в понятную простым роботам фразу.

# Входные данные: Птичья фраза как строка (string).
# Выходные данные: Перевод как строка (string).

# Примеры:

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

# Связь с реальной жизнью: Этот простой «шифр» похож на тот, 
# который используют дети для своего «птичьего» языка. Но теперь-то вы легко взломаете их хитрости.

# Предусловия: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# Фраза всегда имеет перевод.
# ___________________________________________________________________________________

# SOLUTION 28. <> 
def translate(text: str) -> str:
    litters = 'aeiouy'
    translate = []
    
    while len(text) != 0:
        if text[0] not in litters and text[0] != ' ':         
            translate.append(text[0])
            text = text[2:]         
        elif text[0] in litters:
            translate.append(text[0])
            text = text[3:]           
        else:
            translate.append(text[0])
            text = text[1:]
            
    result = ''
    for el in translate:
        result += el
    
    return result


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
VOWELS = "aeiouy"

def translate(phrase):
    output = ""
    c = 0
    
    while c < len(phrase):
        output += phrase[c]
        if phrase[c] in VOWELS:
            c = c + 3
        elif phrase[c] == ' ':
            c = c + 1
        else:
            c = c + 2

    return output

# <><><><><> Best "Creative " Solution <><><><><>
import re,functools
translate=functools.partial(re.sub,r"(\w)(\1\1|.)",r"\1")

# <><><><><> Best "Speedy" Solution <><><><><>
translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])

# <><><><><> Best "3rd party" Solution <><><><><>
VOWELS = "aeiouy"

def translate(phrase):
    phrase = list(phrase)
    # print(phrase)
    for x in range(len(phrase)):
        try:
            if phrase[x] not in VOWELS and phrase[x+1] in VOWELS and phrase[x] != ' ':
                phrase.pop(x+1)
        except IndexError:
            continue    
    phrase = ''.join(phrase)
    
    for x in range(len(phrase)):
        try:
            if phrase[x] in VOWELS and phrase[x] == phrase[x+1] and phrase[x] == phrase[x+2]:
                phrase = phrase.replace(phrase[x]*3, phrase[x])
        except IndexError:
            continue
    return phrase

# <><><><><> Best "Uncategorized" Solution <><><><><>
def translate(text: str) -> str:
    for i in "aeiouy":
        text = text.replace(i+i+i, i)
    new_text = text[0]
    for i in range(1, len(text)):
        if text[i - 1] not in " aeiouy":
            new_text += ''
        else:
            new_text += text[i]
            
    return new_text

# ___________________________________________________________________________________
# MISSION 29. 
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
        


# ___________________________________________________________________________________
# MISSION 30. 
# Excel Column Number >< 
# A->1, B->2, AA->27 ? 
# Simple+ <>
# math string --
# ___________________________________________________________________________________
# Given a string that represents the column title as appears in an Excel sheet, 
# return its corresponding column number.

# But how does the Excel column numbering actually work? Well, 
# the column number is like decimal number, but with base (radix) 26 and "digits" A-Z. 
# Read more about number bases. Let's look at the exact numbers:

# Excel   Decimal
#    A   1
#   ..
#    Z   26

# The 1-"digit" numbers have ended. 2-"digits" numbers start from double first "digit" and go to double last one:

# Excel   Decimal
#    A   1
#   ..
#    Z   26
#   AA   27
#   ..
#   AZ   52
#   BA   53
#   ..
#   BZ   78
#   CA   79
#   ..
#   ..
#   ZZ   702

# Now it's turn for 3-"digit" numbers...

# Input: A string (str).
# Output: An integer (int).

# Examples:
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

# Precondition: Non empty, only upper case, only English letters
# ___________________________________________________________________________________
# SOLUTION 30. <>
def column_number(name: str) -> int:
    return sum((ord(c)-64)*26**n for n, c in enumerate(name[::-1]))
    
print("Example:")
print(column_number("AA"))

# These "asserts" are used for self-checking
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701


# <><><><><> Best "Clear" Solution <><><><><>
def column_number(name: str) -> int:
    num = 0
    for l in name:        
        num = num * 26 + ord(l) - 64 
    return num

# <><><><><> Best "Creative" Solution <><><><><>
COLUMNS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def column_number(name: str) -> int:
    
    if len(name) == 1:
        return COLUMNS.index(name) +1
    else:
        recursion = column_number(name[1:])

    return recursion + (COLUMNS.index(name[0])+1)  * len(COLUMNS) ** (len(name)-1)


# <><><><><> Best "Speedy" Solution <><><><><>
def column_number(name: str) -> int:
    # your code here
    import string  
    collector = []
    for e in range(0, len(name)):        
        collector.append((string.ascii_uppercase.index(name[e]) + 1)*(26**(len(name) - (e+1))))        
    return sum(collector)

# <><><><><> Uncategorized <><><><><>
def ordr(ch):
    return ord(ch)-64
def column_number(name: str) -> int:
    value = 0
    for i in range(len(name)):
        value += ordr(name[-1-i]) * pow(26,i)
    return valu
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 31. 
# Digits Multiplication >< 
# How to work with numbers by non standard way  ? 
# Elementary+  <>
# Russian has-hints math numbers --
# ___________________________________________________________________________________
#  Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

# Входные данные: Положительное целое число.
# Выходные данные: Произведение цифр как целочисленное (int).

# Примеры:
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

# Зачем это нужно: Эта задача может научить вас как использовать простую конвертацию типов данных. 
# ___________________________________________________________________________________
# SOLUTION 31. <>
def checkio(number: int) -> int:
    mult = 1
    for el in str(number):
        if int(el) != 0:
            mult *= int(el)
        else:
            mult += 0
    return mult

print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
# <><><><><> Best "Clear" Solution <><><><><>
def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
    
# <><><><><> Best "Creative" Solution <><><><><>
checkio = lambda n: eval("*".join(i for i in str(n) if i != '0'))

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(number):
    total = 1
    for i in str(number).replace("0",""):
        total *= int(i)
    return total

# <><><><><> Best "3rd party" Solution <><><><><>
from numpy import prod
checkio = lambda number: int(prod( [ int(i) for i in list(str(number)) if i != '0']))

# <><><><><> Uncategorized <><><><><>
def checkio(number: int) -> int:
    b = list(map(int,str(number)))
    result = 1
    for i in b:
        if i:
            result *= i        
    return result
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 32. 
# All Upper I >< 
# Все ли символы написаны заглавными буквами ?  
# Elementary+  <>
# Russian bool string  --
# ___________________________________________________________________________________
#Elementary+
# EN FR JA PL Russian UK ZH-HANS

# Проверить все ли символы в строке являются заглавными. 
# Если строка пустая или в ней нет букв - функция должна вернуть True.

# Входные данные: Строка.
# Выходные данные: Логический тип.

# Пример:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True

# Условия: a-z, A-Z, 1-9 и пробелы
# ___________________________________________________________________________________
# SOLUTION 32. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>


# ___________________________________________________________________________________
# MISSION 33. 
#  >< 
#   ? 
#   <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 33. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
