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
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 4. <>

# <><><><><>  <><><><><>
# ___________________________________________________________________________________
# ___________________________________________________________________________________
# MISSION 5. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 5. <>

# <><><><><>  <><><><><>
# ___________________________________________________________________________________
