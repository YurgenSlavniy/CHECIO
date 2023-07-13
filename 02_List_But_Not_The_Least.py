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
def is_ascending(items: list[int]) -> bool:
    for index, item in enumerate(items):
        try:
            if items[index+1] > item:
                continue
            else:
                return False
        except IndexError:
            break
    return True
    
print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False

# <><><><><> Best "Clear" Solution <><><><><>
from typing import Iterable

def is_ascending(items: Iterable[int]) -> bool:
    return all(items[i] < items[i+1] for i in range(len(items)-1))

# <><><><><> Best "Creative" Solution <><><><><>
is_ascending = lambda l: all(map(int.__lt__, l, l[1:]))

# <><><><><> Best "Speedy" Solution <><><><><>
def is_ascending(items):
    return all(items[i] < items[i+1] for i in range(len(items) - 1))

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    try:
        return np.prod(np.gradient(items)>0)
    except ValueError:
        return True

# <><><><><> Uncategorized  <><><><><>
from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    return sorted(list(set(items))) == items

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 10. 
# Shorter Set >< 
# Remove elements from set from both sides ? 
# Elementary <>
# Set --
# ___________________________________________________________________________________
# Elementary
# English UK

# In a given set of integers, you need to remove minimum and maximum elements.
# The second argument tells how many min and max elements should be removed.

# Input: Two arguments. Set of ints and int.
# Output: Set of ints

# Example:
# assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
# assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
# assert remove_min_max({8, 9, 7}, 2) == set()
# assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}

# How it’s used: (math is used everywhere)
# Precondition: ints in the set is between -1000 and 1000; the second argument is between -1000 and 1000
# ___________________________________________________________________________________
# SOLUTION 10. <>
def remove_min_max(data: set[int], total: int) -> set[int]:
    if total:
        return set(sorted(data)[total:-total])
    return data

print("Example:")
print(remove_min_max({4, 5, 6, 7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

# <><><><><> Best "Clear" Solution <><><><><>
def remove_min_max(data: set, total:int) -> set:
    if total:
        return set(sorted(data)[total:-total])
    return data

# <><><><><> Best "Creative" Solution <><><><><>
remove_min_max=lambda d,t:set([*sorted(d),0][t:-1-t])

# <><><><><> Best "Speedy" Solution <><><><><>
def remove_min_max(data: set, total:int) -> set:
    
    # the next 4 functions are taken from median
    def swap(i, j):
        data[i], data[j] = data[j], data[i]

    def reorder(i, j):
        if data[j] < data[i]:
            swap(i, j)

    def partition_mo3_3way(left, right):
        mid = (left + right) // 2
        reorder(left, mid)
        reorder(left, right)
        reorder(right, mid)
        pivot = data[right]

        i, j, p = left, left, right
        while i < p:
            if data[i] < pivot:
                swap(i, j)
                i += 1
                j += 1
            elif data[i] == pivot:
                p -= 1
                swap(i, p)
            else:
                i += 1

        l = min(p - j, right - p + 1)
        swap(slice(j, j + l), slice(right - l + 1, right + 1))
        return j, j + right - p

    def quickselect(k, left=0, right=len(data) - 1):
        while True:
            if left == right:
                return data[left]
            pivot_l, pivot_r = partition_mo3_3way(left, right)
            if pivot_l <= k <= pivot_r:
                return data[k]
            elif k < pivot_l:
                right = pivot_l - 1
            else:
                left = pivot_r + 1

    if len(data) - 2*total <= 0:
        return set()
    else:
        data = list(data)
        start, stop = total, len(data) - total
        quickselect(start)
        quickselect(stop, left=start+1)
        return set(data[start:stop])
    
# <><><><><> Clear solution <><><><><>
def remove_min_max(data: set, total:int) -> set:

    sorted_data = sorted(data)
    min_data = set(sorted_data[:total])
    max_data = set(sorted_data[len(data)-total:])
    return data - min_data - max_data

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 11. 
# Sum by Type >< 
# Values should be summed differently for different types? 
# Elementary+ <>
# List string iter Array Int --
# ___________________________________________________________________________________
# Elementary+
# English UK

# You have a list. Each value from that list can be either a string or an integer.
# Your task here is to return two values. The first one is a concatenation of all strings from the given list.
# The second one is a sum of all integers from the given list.

# Input: A list of strings and integers.
# Output: A list or tuple.

# Examples:
# assert list(sum_by_types([])) == ["", 0]
# assert list(sum_by_types([1, 2, 3])) == ["", 6]
# assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
# assert list(sum_by_types(["1", "2", 3])) == ["12", 3]

# How it’s used: Input the values of different types and different operations with them,
# depending of type, is the usual thing in development.

# ___________________________________________________________________________________
# SOLUTION 11. <>
from typing import Tuple

def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    ints = 0
    strs = ''
    for item in items:
        if type(item) is int:
            ints += item
        else:
            strs += item
    return (strs, ints)

print("Example:")
print(list(sum_by_types([])))

assert list(sum_by_types([])) == ["", 0]
assert list(sum_by_types([1, 2, 3])) == ["", 6]
assert list(sum_by_types(["1", 2, 3])) == ["1", 5]
assert list(sum_by_types(["1", "2", 3])) == ["12", 3]
assert list(sum_by_types(["1", "2", "3"])) == ["123", 0]
assert list(sum_by_types(["size", 12, "in", 45, 0])) == ["sizein", 57]

# <><><><><> Best "Clear" Solution <><><><><>
def sum_by_types(items):
    result = ['', 0]
    for item in items:
        result[isinstance(item, int)] += item
    return result

# <><><><><> Best "Creative" Solution <><><><><>
import collections, operator
class Neutral(dict): __missing__ = staticmethod(lambda T: T())
report = operator.itemgetter(str, int)

def sum_by_types(a: list) -> report:
    accum = Neutral()
    for elem in a: accum[type(elem)] += elem
    return report(accum)

# <><><><><> Best "Speedy" Solution <><><><><>
from typing import List, Tuple

def sum_by_types(items: List) -> Tuple[str, int]:
    result = ['', 0]
    for item in items:
        result[type(item)==int] += item
    return tuple(result)

# <><><><><> Uncategorized  <><><><><>
def sum_by_types(items):
    str_conc = ''
    int_sum = 0
    for i in items:
        if type(i) == str:
            str_conc = str_conc + i
        else:
            int_sum = int_sum + i       
    return [str_conc, int_sum]

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 12. 
# Sum Numbers >< 
# Просуммируйте числа ? 
# Elementary <>
# Russian string numbers --
# ___________________________________________________________________________________
# Elementary
# EN PL Russian UK

# Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. 
# Если число является частью слова, то его суммировать не нужно.

# Текст состоит из чисел, пробелов и букв английского алфавита.
# Входные данные: Строка.
# Выходные данные: Целое число.

# Пример:
# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#    sum_numbers(
#        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#    )
#    == 3755
#)

# ___________________________________________________________________________________
# SOLUTION 12. <>
def sum_numbers(text: str) -> int:
    sum = 0
    spltxt = text.split(' ')
    for el in spltxt:
        if el.isdigit():
            sum = sum + int(el)          
    return sum

print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

# <><><><><> Best "Clear" Solution <><><><><>
sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

# <><><><><> Best "Creative" Solution <><><><><>
sum_numbers=lambda t,r=__import__("re").compile(r'\b\d+\b'):sum(map(int,r.findall(t)))

# <><><><><> Best "Speedy" Solution <><><><><>
def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))

# <><><><><> Best "3rd party" Solution <><><><><>
def sum_numbers(text: str) -> int:
    import numpy as np
    l = text.split(' ')
    n = np.array([])
    for i in l:
        try:
            n = np.append(n,int(i))
        except:
            p = 0            
    return (int(n.sum()))

# <><><><><> Uncategorized  <><><><><>
import re
def sum_numbers(text: str) -> int:
    nums = re.findall(r"\b\d+\b", text)
    return sum(list(map(int, nums)))

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 13. 
# Easy Unpack >< 
# Верните первый, третий и второй с конца элемент из заданого массива ? 
# Elementary <>
# Russian math numbers has-Hints Array tuple --
# ___________________________________________________________________________________
# Elementary
# EN FR JA Russian UK ZH-HANS

# Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: 
# первого, третьего и второго с конца элементов заданного кортежа.

# Важно отметить, что вам нужно использовать индекс для извлечения элементов из  кортежа. 
# Обратите внимание, нумерация индексов начинается с 0, не с 1. Это означает,
# что если вы хотите получить первый элемент из кортежа elements , вам нужен elements[0] , а если второй — elements[1] .

# Входные данные: Кортеж длиной не менее 3 элементов.
# Выходные данные: Кортеж.

# Пример:
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# ___________________________________________________________________________________
# SOLUTION 13. <>
def easy_unpack(elements: tuple) -> tuple:
    end_list = []
    end_list.append(elements[0]) 
    end_list.append(elements[2]) 
    end_list.append(elements[-2])
    return tuple(end_list)


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# <><><><><> Best "Clear" Solution <><><><><>
from operator import itemgetter
easy_unpack = itemgetter(0, 2, ~1)

# <><><><><> Best "Creative" Solution <><><><><>
easy_unpack = lambda t: (t[0], t[2], t[-2])

# <><><><><> Best "Speedy" Solution <><><><><>
def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def easy_unpack(elements: tuple) -> tuple:
    arr = np.array(elements)
    return tuple(arr[[0,2,-2]])

# <><><><><> Uncategorized <><><><><>
def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    a=elements[0]
    b=elements[2]
    c=elements[-2]
    g=(a,b,c)
    return g

# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 14. 
# Majority >< 
# Check if the majority of elements are true ? 
# Elementary+ <>
# bool list --
# ___________________________________________________________________________________
# We have a list of booleans. Let's check if the majority of elements are True.

# Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount, function should return False.

# Input: A list of booleans.
# Output: A Boolean.

# Examples:
# assert is_majority([True, True, False, True, False]) == True
# assert is_majority([True, True, False]) == True
# assert is_majority([True, True, False, False]) == False
# assert is_majority([True, True, False, False, False]) == False

# ___________________________________________________________________________________
# SOLUTION 14. <>
def is_majority(items: list[bool]) -> bool:
    true_count = 0
    false_count = 0
    for i in items:
        if i == True:
            true_count += 1
        else:
            false_count += 1
    if true_count > false_count:
        return True
    else:
        return False
    
print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False


# <><><><><> Best "Clear" Solution <><><><><>
def is_majority(items: list) -> bool:
    return sum(items) > len(items) / 2

# <><><><><> Best "Creative" Solution <><><><><>
is_majority=lambda z:sum([-1,1][i]for i in z)>0

# <><><><><> Best "Speedy" Solution <><><><><>
def is_majority(items: list) -> bool:
    
    return items.count(True) > items.count(False)

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def is_majority(items: list) -> bool:
    return True if np.sum(np.array(items)) > len(items)/2 else False

# <><><><><> Uncategorized <><><><><>
def is_majority(items: list) -> bool:
    true_count = items.count(True)
    false_count = items.count(False)
    if true_count > false_count:
        return True
    else:
        return False

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 15. 
# Median >< 
# Find the mathematical median in a list of numbers ? 
# Elementary+ <>
# Russian has-hints numbers statistics --
# ___________________________________________________________________________________
# Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины. 
# В сортированом массиве с нечётным числом элементов медиана — это число в середине массива. 
# Для массива с чётным числом элементов, где нет одного элемента точно посередине, 
# медиана — это среднее значение двух чисел, находящихся в середине массива.
# В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.

# Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Middle Characters.

# Входные данные: Массив как список (list) чисел (int).
# Выходные данные: Медиана как число (int, float).

# Примеры:
# assert checkio([1, 2, 3, 4, 5]) == 3
# assert checkio([3, 1, 2, 5, 3]) == 3
# assert checkio([1, 300, 2, 200, 1]) == 2
# assert checkio([3, 6, 20, 99, 10, 15]) == 12.5

# Как это используется: Медиана находит свое применение в статистике и теории вероятности, 
# и особенно важна для ассиметричного распределения. 
# Для примера: мы хотим узнать среднее доход населения -- 100 человек получают $100 в месяц и 10 человек получают $1,000,000. 
# Если мы возьмем среднее арифметическое, то получим $91,000.
# Это довольно странное число, не показывающее истинного положения дел. 
# В этом случае медиана будет равна $100, 
# что станет для нас более полезной величиной и покажет более правдоподобную картину. Статья в Википедии.

# Предусловия:
# 1 < len(data) ≤ 1000
# all(0 ≤ x < 10 ** 6 for x in data)

# ___________________________________________________________________________________
# SOLUTION 15. <>
import numpy as np

def checkio(data: list[int]) -> int | float:
    return np.median(data)


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2

# <><><><><> Best "Creative" Solution <><><><><>
checkio=lambda d:(lambda t,n:t[n]+t[-n-1])(sorted(d),len(d)//2)/2

# <><><><><> Best "Speedy" Solution <><><><><>
# Find the k'th-smallest value in a, worst case O(n)
# Skip the first d elements and consider only the next n
def select(a, d, n, k):
    if n <= 5:
        return sorted(a[d:d+n])[k]

    # Find median of medians of 5
    medians = [sorted(a[i:i+5])[2] for i in range(d, d+n-4, 5)]
    m = len(medians)
    median = select(medians, 0, m, m // 2)

    # Partition around the median.
    # a[d:i]     <= median
    # a[j+1:d+n] >= median
    i, j = d, d+n-1
    while i <= j:
        while a[i] < median: i += 1
        while a[j] > median: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if d+k < i: return select(a, d, i-d, k)
    else:       return select(a, i, n+d-i, k+d-i)

def checkio(data):
    n = len(data)
    if n % 2 == 1:
        return select(data, 0, n, n//2)
    else:
        return 0.5 * (select(data, 0, n, n//2-1) + select(data, 0, n, n//2))

# <><><><><> Best "3rd party" Solution <><><><><>
from typing import List
import numpy as np

def checkio(data: List[int]) -> [int, float]:
    return np.median(data)

# <><><><><> Uncategorized <><><><><>
def checkio(data: list[int]) -> int | float:
    # replace this for solution
    m = 0
    m1 = 0
    m2 = 0
    data = sorted(data)
    #data.sort()
    if len(data) % 2 == 0:
        m1 = data[len(data) // 2 -1]
        m2 = data[len(data) // 2]
        m = (m1 + m2) /2
    else:
        m = data[len(data) // 2]
        
    return m

# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 16. 
# Duplicate Zeros >< 
# Слопайте все пончики... упс, удвойте все нули в списке ? 
# Elementary+ <>
# Russian list --
# ___________________________________________________________________________________
# Elementary+
# EN Russian UK

# "Иногда нули напоминают очень вкусные пончики. И каждый раз, доедая пончик, нам хочется ещё один, а потом ещё, и ещё..."

# Перед вами список целых чисел. 
# Ваша задача в этой миссии – продублировать (..., 🍩, ... --> ..., 🍩, 🍩, ...) 
# все нули в данном списке (думайте о пончиках ;-P) и вернуть в виде любого итерируемого объекта. Посмотрим на пример:
# [1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]
    
# Входные данные: Список целых чисел.
# Выходные данные: Список или другой итерируемый объект (кортеж, генератор, итератор) из целых чисел.

# Примеры:
# assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
#   1,
#   0,
#   0,
#   2,
#   3,
#   0,
#   0,
#   4,
#   5,
#   0,
#   0,
# ]
# assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
# assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

# Если вы прошли миссию, можете со спокойной душой насладиться 🍩!=)

# ___________________________________________________________________________________
# SOLUTION 16. <>
from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    idx = 0
    new_list = []
    for el in donuts:
        new_list.append(el)
        if el == 0:
            new_list.append(0)
    return new_list
            
print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]


# <><><><><> Best "Clear" Solution <><><><><>
def duplicate_zeros(donuts: list) -> list:
    # your code here
    return sum([[i] if i else [0 , 0] for i in donuts], [])

# <><><><><> Best "Creative" Solution <><><><><>
from collections.abc import Iterable
from itertools import chain

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    return chain.from_iterable([d] if d else [d, d] for d in donuts)

# <><><><><> Best "Speedy" Solution <><><><><>
from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    for v in donuts:
        if v == 0:
            yield 0
        yield v
    return []

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
def duplicate_zeros(donuts) -> list:
    arr = np.array(donuts)
    for idx, i in enumerate(*list(np.where(arr == 0))):
        donuts.insert(i+idx, 0)
    return donuts

# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    # your code here
    i=0
    aplique=donuts
    a=len(aplique)
    while i <a:
        if aplique[i]== 0:
            aplique.insert(i,0)
            i+=2
            a=len(aplique)
        else: 
            i+=1
   # print(aplique)

    return aplique

# ___________________________________________________________________________________


# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 17. 
# Stock Profit >< 
# Find the best time to buy and the best time to sell ? 
# Elementary+ <>
# game list --
# ___________________________________________________________________________________
# You are a broker on the stock exchange. 
# You've decided to make just one complete operation: 
# to buy a stock and sell it later to make a profit. 
# “Short-selling” (sell first, buy later) is not allowed in this market.

# Buying and selling prices for every distinct moment are the same 
# (in every moment you may either by a stock for price x or sell a stock 
# (if you have it) for the same price x) and are shown in the given list stock.

# So, you have to choose, what are the best prices to buy a stock and later sell
# it to make the maximum profit from the operation.
# Your function must return this maximum possible profit. 
# If it's not possible to make any profit with given prices (it's <= 0), your function should return 0.

# Input: Stock prices as list of integers.
# Output: Maximum possible profit as integer.

# Examples:
# assert stock_profit([2, 3, 4, 5]) == 3
# assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
# assert stock_profit([4, 3, 2, 1]) == 0
# assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4

# Preconditions:

# len(stock) > 1;
# 0 <= price <= 1000.

# ___________________________________________________________________________________
# Вы являетесь брокером на фондовой бирже. 
# Вы решили совершить всего одну завершенную операцию: купить акцию и продать ее позже, 
# чтобы получить прибыль. “Короткие продажи” 
# (сначала продайте, позже купите) на этом рынке запрещены.

# Цены покупки и продажи в каждый отдельный момент одинаковы 
# (в каждый момент вы можете либо приобрести акцию по цене x, либо продать акцию 
# (если она у вас есть) по той же цене x) и указаны в данном списке акций.

# Итак, вы должны выбрать, по каким ценам лучше всего купить акцию, 
# а затем продать ее, чтобы получить максимальную прибыль от операции. 
# Ваша функция должна возвращать эту максимально возможную прибыль. 
# Если невозможно получить какую-либо прибыль при заданных ценах (это <= 0), ваша функция должна возвращать 0.

# Входные данные: Цены на акции в виде списка целых чисел.

# Результат: Максимально возможная прибыль в виде целого числа.

# ___________________________________________________________________________________
# SOLUTION 17. <>
def stock_profit(stock: list[int]) -> int:
    buy_price = stock[0]
    idx_list = range(0, len(stock) - 1)
    idx = 0
    for i in idx_list:
        if stock[i] < buy_price:
            buy_price = stock[i]
            idx = i
    
    new_stock = stock[idx:]
    max_price = max(new_stock)
    return max_price - buy_price

print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0


# <><><><><> Best "Clear" Solution <><><><><>
stock_profit = lambda s: max([s[i] - min(s[:i]) for i in range(1, len(s))] + [0])

# <><><><><> Best "Creative" Solution <><><><><>
stock_profit=p=lambda s:len(s)and max(max(s)-s[0],p(s[1:]))

# <><><><><> Best "Speedy" Solution <><><><><>
def stock_profit(stock: list) -> int:
    n=1
    profits=[0]
    for buy in stock:
        
        for sell in stock[n:]:
            profits.append(sell-buy)
        n+=1
    return max(profits)

# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
def stock_profit(stock: list[int]) -> int:
    mins = stock[0]
    prof = []
    for mins in stock:
        maxs = max(stock[stock.index(mins):])
        prof.append(maxs-mins)
    return max(prof)
# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 18. 
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



# ___________________________________________________________________________________
# MISSION 19. 
# The Most Frequent >< 
# Определите наиболее часто встречающийся элемент в последовательности. ? 
# Elementary <>
# Russian has-hints list statistics --
# ___________________________________________________________________________________
# Elementary
# EN JA Russian UK ZH-HANS
# Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.

# Входные данные: список строк.
# Выходные данные: строка.

# Примеры:
# assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
# assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

# ___________________________________________________________________________________
# SOLUTION 19. <>
def most_frequent(data: list[str]) -> str:
    return max(set(data), key=data.count)
    
print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

# <><><><><> Best "Clear" Solution <><><><><>
from statistics import mode as most_frequent

# <><><><><> Best "Creative" Solution <><><><><>
def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key = data.count)


# <><><><><> Best "Speedy" Solution <><><><><>
def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    mx = 0
    word = ''
    for s in set(data):
        if data.count(s) > mx:
            mx = data.count(s)
            word = s
    return word

# <><><><><> Best "3rd party" Solution <><><><><>
def most_frequent(data: list) -> str:
    """pandas"""
    import pandas as pd

    if not data : return ''
    df = pd.DataFrame(data, columns=['valeurs'])
    dg = df['valeurs'].value_counts()


    return dg.index[0]

# <><><><><> Uncategorized <><><><><>
from collections import Counter
def most_frequent(data: list[str]) -> str:
    dictionary = Counter(data) 
    max_value = 0
    for iterable in dictionary:
        if dictionary[iterable] > max_value:
            max_value = dictionary[iterable]
            max_key = iterable 
    return max_key

# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 20. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 20. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 21. 
# Compress List >< 
# "Compress" a given list ? 
# Elementary+ <>
# list --
# ___________________________________________________________________________________
# Elementary+
# English FR PL UK

# A given sequence should be "compressed" in a way so, instead of two (or more) equal elements, 
# staying one after another, there should be only one in the result sequence.

# example

# Input: List.
# Output: "Compressed" List or another Iterable (tuple, iterator, generator).

# Examples:
# assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
#    5,
#    4,
#    5,
#    6,
#    5,
#    7,
#    8,
#    0,
#]
# assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
# assert list(compress([7, 7])) == [7]
# assert list(compress([])) == []
# ___________________________________________________________________________________
# SOLUTION 21. <>
from collections.abc import Iterable

def compress(items: list[int]) -> Iterable[int]:
    compr_list = []
    
    if len(items) == 0:
        return []
    else:    
        while len(items) != 1:
            if items[0] == items[1]:
                items = items[1:]
                print('one', items, compr_list)
            else:
                compr_list.append(items[0]) 
                items = items[1:]      
                print('Two', items, compr_list)
    compr_list.append(items[0])
    return compr_list
    
print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

# <><><><><> Best "Clear" Solution <><><><><>
from itertools import groupby

def compress(items):
    for key, _ in groupby(items): yield key

# <><><><><> Best "Creative" Solution <><><><><>
import itertools
compress = lambda l: (i for i, _ in itertools.groupby(l))

# <><><><><> Best "Speedy" Solution <><><><><>
compress= lambda x: [x[i] for i in range(len(x)) if i==0 or x[i]!=x[i-1]]

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
from typing import Iterable


def compress(items: list) -> Iterable:

    if len(items) == 0:
        return items
    else:
        different = (np.diff(items) != 0)
        different = np.insert(different, 0, -1)

        return list(np.array(items)[different])


# <><><><><> Uncategorized <><><><><>
from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    if len(items)>0:
        cur = items[0]
        result = [items[0]]
        for item in items:
            if item != cur:
                result.append(item)
                cur = item
    else: result = []    
    return result

# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 22. 
# Remove All After >< 
# Remove all the elements after the given one from array ? 
# Elementary <>
# list numbers --
# ___________________________________________________________________________________
# Elementary
# English FR PL UK

# Not all of the elements are important. 
# What you need to do here is to remove all of the elements after the given one from sequence.

# example
# For illustration, we have a sequence [1, 2, 3, 4, 5] 
# and we need to remove all the elements that go after 3 - which are 4 and 5.

# We have two edge cases here:

# - if a cutting element cannot be found, then the sequence shouldn't be changed;
# - if the sequence is empty, then it should remains empty.

# Input: List of integers (int).
# Output: List or other Iterable (tuple, iterator, generator ...) of integers (int).

# Examples:

assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

# ___________________________________________________________________________________
# SOLUTION 22. <>
from collections.abc import Iterable

def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    result = []
    if border in items:
        for el in items:
            if el != border:
                result.append(el)
            else:
                result.append(el)
                break
    else:
        return items
    
    return result


print("Example:")
print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_after([], 0)) == []
assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 23. 
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

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 24. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 24. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
