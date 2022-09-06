# ___________________________________________________________________________________
# MISSION 1. 
# Is Even >< 
# Check if the given number is even or not. ? 
# Elementary <>
# Int int --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian

# Проверить является ли число четным или нет. 
# Ваша функция должна возвращать True если число четное, и False если число не четное.

# Входные данные: Целое число.
# Выходные данные: Логический тип.

# Пример:
# is_even(2) == True
# is_even(5) == False
# is_even(0) == True

# Где это используется: (математика используется везде)
# Условия: целые числа даны в диапазоне от -1000 и до 1000
# ___________________________________________________________________________________
# SOLUTION 1. <>
def is_even(num: int) -> bool:
    if num %2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    
# <><><><><> Best "Clear" Solution <><><><><>
def is_even(num: int) -> bool:
    return num & 1 == 0
  
# <><><><><> Best "Creative" Solution <><><><><>
def is_even(num: int) -> bool:
    return bin(num)[-1]=='0'

# <><><><><> Best "Speedy" Solution <><><><><>
def is_even(num: int) -> bool:
    return not(num & 1)

# <><><><><> Uncategorized <><><><><>
def is_even(num: int) -> bool:
    return num % 2 == 0
  
# <><><><><> Uncategorized <><><><><>  
def is_even(num: int) -> bool:
    div, mod = divmod(num, 2)
    return mod == 0

# ___________________________________________________________________________________
# MISSION 2. 
# Replace Last >< 
# The last element should become the first one ? 
# Elementary <>
# List --
# ___________________________________________________________________________________
# Elementary
# English

# In a given list the last element should become the first one. An empty list or list with only one element should stay the same

# Input: List.
# Output: Iterable.

# Example:

# replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
# replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
# replace_last([1]) == [1]
# replace_last([]) == []
# ___________________________________________________________________________________
# SOLUTION 2. <>
def replace_last(line: list) -> list:
    if line == []:
        return line
    else:
        last = line[-1]
        new_list = []
        new_list.append(last)
        result = new_list + line[:-1]
        return result


if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    
# <><><><><> Best "Creative" Solution <><><><><>
def replace_last(line: list) -> list:
    # pop off the last item and insert it at the front -> profit
    return [line.pop()] + line if line else []

# <><><><><> Best "Speedy" Solution <><><><><>
def replace_last(items):
    if items:
        yield items[-1]
        for i in range(len(items)-1):
            yield items[i]

# <><><><><> Best "Clear" Solution <><><><><>
# Change items IN-PLACE.
def replace_last(items: list) -> list:
    if items:
        items.insert(0, items.pop())
    return items

# Slices
def replace_last(items: list) -> list:
    return items[-1:] + items[:-1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_last(items: list) -> deque:
    items = deque(items)
    items.rotate(1)
    return items

# <><><><><> Uncategorized  <><><><><>
def replace_last(line: list) -> list:
    if not line:
        return line
    ret = [line[-1]] + line[:-1]
    return ret

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 3. 
# First Word >< 
# Find the first word in a string ? 
# Elementary+ <>
# String Text Has-Hints --
# ___________________________________________________________________________________
# Elementary+
# Russian EN JA
# I might see a simplified version of this mission already First Word (simplified) .
# This mission is a little bit more complex as not only English letters can be in the given string.

# Дана строка и нужно найти ее первое слово.

# При решении задачи обратите внимание на следующие моменты:
# - В строке могут встречатся точки и запятые
# - Строка может начинаться с буквы или, к примеру, с пробела или точки
# - В слове может быть апостроф и он является частью слова
# - Весь текст может быть представлен только одним словом и все

# Входные параметры: Строка.
# Выходные параметры: Строка.

# Пример:
# first_word("Hello world") == "Hello"
# first_word("greetings, friends") == "greetings"

# How it is used: first word is a command in command line
#Precondition: text can contain a-z A-Z , .
# ___________________________________________________________________________________

# SOLUTION 3. <>
def first_word(text: str) -> str:
    prep_text = text.replace(',', ' ').replace('.', ' ')
    text_split = prep_text.split()
    return text_split[0]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    
# <><><><><> Best "Clear" Solution <><><><><>
import re
def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)

# <><><><><> Best "Creative" Solution <><><><><>
first_word = lambda t: ''.join([x, ' '][x in '.,'] for x in t).split()[0]

# <><><><><> Best "Speedy" Solution <><><><><>
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':
        j += 1
    return text[i:j]

# <><><><><> Uncategorized <><><><><>
def first_word(text):
    return text.replace(',', ' ').replace('.', ' ').split()[0]

# <><><><><> Uncategorized <><><><><>
def first_word(text: str) -> str:   
    import re
    text = text.strip(' .,')
    text = re.split(r'[\s,\,,\.]+',text,0,re.I)
    return text[0]

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 4. 
# All the Same >< 
# Check if all elements are the same ? 
# Simple <>
# List logic --
# ___________________________________________________________________________________
# Simple
# EN JA Russian UK ZH-HANS

# We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. 
# In order to see all other solutions you should change the filter.
# В этой миссии Вам надо определить, все ли элементы массива равны.

# Входные: List.
# Выходные: Bool.

# Примеры:
# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

# Precondition: all elements of the input list are hashable
# ___________________________________________________________________________________
# SOLUTION 4. <>
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 0 or len(elements) == 1:
        return True
    else:
        set_elements = set(elements)
        if len(set_elements) == 1:
            return True
        else:
            return False
        
if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    
# <><><><><> Best "Creative" Solution <><><><><>
all_the_same = lambda e: e[1:] == e[:-1]

# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List, Any
from numpy import unique

def all_the_same(elements: List[Any]) -> bool:
    return len(unique(elements)) <= 1

# <><><><><> Uncategorized  <><><><><>
def all_the_same(elements: List[Any]) -> bool:
    len_elements = len(elements)
    if len_elements == 0:
        return True
    else:
        for i in elements:
            same = elements.count(i)
        
            if same < len_elements:
                return False
            else:
                return True
            
# <><><><><> Clear <><><><><>
from operator import eq
from itertools import starmap

def all_the_same(elements):
    return all(starmap(eq, zip(elements, elements[1:])))
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 5. 
# Even the Last >< 
# How to work with arrays indexes. ? 
# Elementary <>
# Russian math numbers has-Hints --
# ___________________________________________________________________________________
# Elementary
# DE ES HU IT PT-BR Russian ZH-HANS FR FA PL PT UK EN JA EL

# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), 
# затем перемножить эту сумму и последний элемент исходного массива. 
# Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).

# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int).

# Примеры:

# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0

# Зачем это нужно: Индексы и срезы - очень важные элементы программирования,
# как на Python, так и на других языках. Это поможет вам в дальнейшем.

# Предусловия: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# ___________________________________________________________________________________
# SOLUTION 5. <>

def checkio(array):
#    from numpy import sum
    if len(array) > 0:
        return int(sum(array[::2])*array[-1])
    else:
        return 0
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    
# <><><><><> Best "Clear" Solution <><><><><>
def checkio(array):
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

# <><><><><> Best "Creative" Solution <><><><><>
checkio = lambda array: sum(array[::2]) * sum(array[-1:])

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(array):
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0

# <><><><><> Best "3rd party" Solution <><><><><>
def checkio(array):
    from numpy import sum
    if len(array) > 0:
        return int(sum(array[::2])*array[-1])
    else:    
        return 0
    
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 6. 
# Right to Left >< 
# “Left, right, left, right, left, left, left. Your destination is on the left.” “Wait, this isn’t where I was going…” ? 
# Elementary <>
# Russian string parsing has-Hints --
# ___________________________________________________________________________________
#  Elementary
# PL DE JA Russian UK EN ES IT EL FR

# "На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
# Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
# "Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"."
# Scientific American. www.scientificamerican.com

# Один робот был занят простой задачей: 
# объединить последовательность строк в одно выражение для создания инструкции по обходу корабля. 
# Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
# Дана последовательность строк. Вы должны объединить эти строки в блок текста, 
# разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, 
# вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

# Входные данные: Последовательность строк.
# Выходные данные: Текст, как строка.

# Пример:
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"

# Как это используется: Это просто пример операций, использующих строки и последовательности.
# Предусловие:
# 0 < len(phrases) < 42
# ___________________________________________________________________________________
# SOLUTION 6. <>
def left_join(message_text):
    join_mess = ','.join(message_text)
    replace = join_mess.replace('right', 'left')
    return replace


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

# <><><><><> Best "Clear" Solution <><><><><>
def left_join(phrases):
    return (",".join(phrases)).replace("right","left")

# <><><><><> Best "Creative" Solution <><><><><>
def left_join(phrases):
    return ','.join(map(lambda x:x.replace('right','left'),phrases))

# <><><><><> Best "Speedy" Solution <><><><><>
def left_join(phrases):
    return ",".join(phrases).replace("right", "left")

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

class right_to_left():
    def __init__(self, phrases):
        self.phrases = phrases

    def perform(self):
        replaced_words_array = np.array([p.replace('right', 'left') for p in self.phrases])
        replaced_words_list = replaced_words_array.tolist()
        return ",".join(replaced_words_list)

def left_join(phrases: tuple) -> str:
    foo = right_to_left(phrases)
    return foo.perform()

# <><><><><> "Creative" Solution <><><><><>
def left_join(phrases):
    a=""
    for i in phrases:
        a=a+","+i
    a=a[1:].replace("right", "left")
    return a
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 7. 
# Backward Each Word >< 
# Развернуть каждое слово заданной строки ? 
# Elementary+ <>
# Russian string --
# ___________________________________________________________________________________
# Elementary+
# EN Russian UK

# Требуется обратить порядок букв в каждом слове предоставленной строки, 
# так чтобы слова остались на своих местах.

# Входные данные: строка.
# Выходные данные: строка.

# Примеры:
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"

# Предусловие: Строка состоит только из символов алфавита и пробелов
# ___________________________________________________________________________________
# SOLUTION 7. <>
def backward_string_by_word(text: str) -> str:
    i = 0
    result = []
    for j in range(len(text)):
        if text[j] == ' ': 
            word = text[i:j]
            result.append(word[::-1])
            result.append(' ')
            i = j+1
        elif j == len(text)-1:
            word = text[i:j+1]
            result.append(word[::-1])
        else:
            continue
    result = ''.join(result)
    return result

print("Example:")
print(backward_string_by_word(""))

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

# <><><><><> Best "Clear" Solution <><><><><>
def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))

# <><><><><> Best "Creative" Solution <><><><><>
def backward_string_by_word(text: str) -> str:
  return ' '.join(map(lambda x: x[::-1], text.split(' ')))

# <><><><><> Best "Speedy" Solution <><><><><>
def backward_string_by_word(text: str) -> str:
    return ' '.join([i[::-1] for i in text.split(' ')])

# <><><><><> Uncategorized <><><><><>
import re

def backward_string(match_object) -> str:
    return match_object.group(0)[::-1]

def backward_string_by_word(text: str) -> str:
    return re.sub(r"\w+", backward_string, text)

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 8. 
# Non Empty Lines >< 
# How many non-empty lines a given text has? 
# Elementary <>
# String text multiline --
# ___________________________________________________________________________________
# Elementary
# English UK

# You need to count how many non-empty lines a given text has.
# An empty line is a line without symbols or the one that contains only spaces.

# Input: A text.
# Output: An int.

# Example:
# assert non_empty_lines("one simple line\n") == 1
# assert non_empty_lines("") == 0
# assert non_empty_lines("\nonly one line\n            ") == 1
# assert ( non_empty_lines(
#        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
#    )
#    == 3
# )
# ___________________________________________________________________________________

# SOLUTION 8. <>
def non_empty_lines(text: str) -> int:
    lines = text.splitlines()
    while '' in lines:
        lines.remove('')
    count = 0
    for i in lines:
        if i.isspace():
            count += 1
    return len(lines) - count

print("Example:")
print(non_empty_lines("one simple line\n"))

assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)
# <><><><><> Best "Creative" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return 0 if not text else len(list(filter(None, map(lambda i: i.strip(),
        __import__('re').split('\n', text)))))

# <><><><><> Best "Clear" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return sum(bool(line.strip()) for line in text.splitlines())

# <><><><><> Best "Speedy" Solution <><><><><>
def non_empty_lines(text: str) -> int:
    return len([x for x in text.split('\n') if any(i.isalha() for i in x)])

# <><><><><> Uncategorized <><><><><>
def non_empty_lines(text: str) -> int:
    if len(text) == 0:
        return 0
    line_list = text.split('\n')
    counter = 0
    for each in line_list:
        if len(each.strip()) > 0:
            counter += 1
    return counter

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 9. 
# Ascending List >< 
# The sequence of elements items is ascending ? 
# Elementary+ <>
# ListBool --
# ___________________________________________________________________________________
# Elementary+
# English UK

# Determine whether the list of elements is ascending such that each of its elements is strictly 
# larger than (and not merely equal to) the preceding element. Empty list consider as ascending.

# Input: List with ints.
# Output: Bool.

# Example:
# assert is_ascending([-5, 10, 99, 123456]) == True
# assert is_ascending([99]) == True
# assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
# assert is_ascending([]) == True

# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
# ___________________________________________________________________________________
# SOLUTION 9. <>

# <><><><><>  <><><><><>
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 10. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 10. <>

# <><><><><>  <><><><><>
# ___________________________________________________________________________________
