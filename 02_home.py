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

# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
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

# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 15. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 15. <>

# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# <><><><><>  <><><><><>
# ___________________________________________________________________________________
