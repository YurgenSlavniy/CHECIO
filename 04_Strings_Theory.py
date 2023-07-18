# ___________________________________________________________________________________
# MISSION 1. 
# Between Markers >< 
# Найти подстроку между маркерами? 
# Elementary+ <>
# Russian has-hints parsing string--
# ___________________________________________________________________________________
# Elementary+
# EN JA Russian UK
# Вам дана строка и два маркера (начальный и конечный). 
# Вам необходимо найти текст, заключенный между двумя этими маркерами. 
# Но есть несколько важных условий:

# - Начальный и конечный маркеры всегда разные
# - Если нет начального маркера, то началом считать начало строки
# - Если нет конечного маркера, то концом считать конец строки
# - Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
# - Если конечный маркер стоит перед начальным, то вернуть пустую строку

# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
# Output: Строка.

# Примеры:
assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"

# Как это использутеся: может использоваться для парсинга небольшой верстки

# Предусловия: не может быть более одного маркера одного типа
# ___________________________________________________________________________________
# SOLUTION 1. <>
def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text:
        return text[text.find(begin) + len(begin):text.find(end)]
    elif begin not in text and end in text:
        return text[:text.find(end)]
    elif end not in text and begin in text:
        return text[text.find(begin)+ len(begin):]
    else:
        return text
 

print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]

# <><><><><> Best "Creative" Solution <><><><><>
def between_markers(txt, begin, end):
    a, b, c = txt.find(begin), txt.find(end), len(begin)
    return [txt[a+c:b], txt[a+c:], txt[:b], txt][2*(a<0)+(b<0)]

# <><><><><> Best "Speedy" Solution <><><><><>
between_markers = lambda text, begin, end: text[text.index(begin)+len(begin) if begin in text else 0: text.index(end) if end in text else len(text)]

# <><><><><> Best "3rd party" Solution <><><><><>

# <><><><><> Uncategorized <><><><><>
def between_markers(text, marker1, marker2):
    if marker1 not in text:
        start = 0
    else:
        start = text.index(marker1) + len(marker1)

    if marker2 not in text:
        end = len(text)
    else:
        end = text.index(marker2)

    if end < start:
        return ""
    else:
        return text[start:end]
# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 2. 
# Correct Capital >< 
# Check whether the register is used correctly. ? 
# Elementary+ <>
# bool logic string --
# ___________________________________________________________________________________
#  Elementary+
# English UK

# You are given a word in which letters can be in different cases. 
# Your task is to check whether the case was used correctly in the line. 
# If everything is correct - return True, if there are errors - return return False.

# Examples of the correct use of cases:

# All characters in the string are in uppercase. For example, "CHECKIO";
# None of the characters are in uppercase. For example, "checkio";
# Only the first character is in uppercase. For example, "Checkio".

# Вам дается слово, в котором буквы могут быть в разных падежах.
# Ваша задача - проверить, правильно ли был использован регистр в строке. 
# Если все правильно - верните True, если есть ошибки - верните return False.

# Примеры правильного использования падежей:

# Все символы в строке набраны в верхнем регистре. Например, "CHECKIO";
# Ни один из символов не написан заглавными буквами. Например, "checkio";
# В верхнем регистре указан только первый символ. Например, "Checkio".

# Input: String.
# Output: Bool.

# Examples:

assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True
# ___________________________________________________________________________________
# SOLUTION 2. <>
def correct_capital(line: str) -> bool:
    c1 = line[0].isupper()
    c2 = line[1:].isupper()
    c3 = line[1:].islower()
    c4 = line.islower()
    
    return (c1 and c2) or (c1 and c3) or c4


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

# <><><><><> Best "Clear" Solution <><><><><>
correct_capital = lambda s: s in {s.upper(), s.lower(), s.capitalize()}

# <><><><><> Best "Creative" Solution <><><><><>
correct_capital = lambda line: line in (line.capitalize(), line.upper(), line.lower())

# <><><><><> Best "Speedy" Solution <><><><><>
import re
from string import ascii_lowercase, ascii_uppercase

_l = rf'[{ascii_lowercase}]'
_u = rf'[{ascii_uppercase}]'
incorrect = re.compile(rf'({_l}{_u})|(\b{_u}{{2,}}{_l})')

def correct_capital(line: str) -> bool:
    return not incorrect.search(line)
    
# <><><><><> Uncategorized <><><><><>
def correct_capital(line: str) -> bool:
    # your code here
    return any ([line == line.upper(), line ==line.lower(), line==line[0]+line[1:].lower()])

# ___________________________________________________________________________________


# ___________________________________________________________________________________
# MISSION 3. 
# Long Repeat >< 
# Найдите длину самой длинной подстроки, которая состоит из одного и того же символа. ? 
# Elementary+ <>
# Russian parsing string text --
# ___________________________________________________________________________________
#  Elementary+
# EN Russian UK ZH-HANS

# Существует четыре миссии связанные с анализом частей строки. 
# Все они были созданы за один день и не требуют более одного дня для своего решения. 
# Эти миссии можно с легкостью преодолеть посредством простого перебора символов. 
# Но, возможно, есть вариант получше? (У Вас может еще не быть доступа ко всем этим миссиям, 
# но по мере открытия островов на карте он будет предоставлен)

# Это первая миссия из серии. Вам необходимо найти длину самой длинной подстроки,
# которая состоит из одинаковых букв. 
# Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". 
# Последняя подстрока является самой длинной, что и делает ее ответом.

# Входные данные: Строка.
# Выходные данные: Целое число.

# Пример:
assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3
# ___________________________________________________________________________________
# SOLUTION 3. <>

def long_repeat(line: str) -> int:
    max_count = 1
    count = 1
   
    if len(line) == 0:
        return 0
    else:
        while len(line) > 1:
            if line[0] == line[1]:
                count += 1
                line = line[1:]
                if count > max_count:
                    max_count = count
            else:
                count = 1 
                line = line[1:]
            
    return max_count


print("Example:")
print(long_repeat("sdsffffse"))

assert long_repeat("sdsffffse") == 4
assert long_repeat("ddvvrwwwrggg") == 3

# <><><><><> Best "Clear" Solution <><><><><>
from itertools import groupby
def long_repeat(line):
    """length the longest substring that consists of the same char"""
    return max(len(list(g)) for _, g in groupby(line)) if line else 0

# <><><><><> Best "Creative" Solution <><><><><>
long_repeat=lambda l:len(l)and max(map(len,dict(__import__('re').findall(r'((.)\2*)',l))))

# <><><><><> Best "Speedy" Solution <><><><><>
from itertools import groupby

def long_repeat(string):
    if not string: return 0
    return max(len(list(g)) for _,g in groupby(string))

# <><><><><> Best "3rd party" Solution <><><><><>
def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    import numpy as np
    return max([len(_) for _ in np.split(list(line), [i+1 for i, letter in enumerate(list(line)[:-1]) if list(line)[i] != list(line)[i+1]])])

# <><><><><> Uncategorized <><><><><>
def long_repeat(line: str) -> int:
    max_count = 0
    cur_count = 0
    for i in range(len(line)):
        if i == 0 or line[i] != line[i - 1]:
            cur_count = 1
        else:
            cur_count += 1
        max_count = max(max_count, cur_count)
    return max_count


# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 4. 
# All Upper II >< 
# Checks if the string is a valid number ? 
# Elementary <>
# bool string --
# ___________________________________________________________________________________
# Elementary
# English FR PL UK ZH-HANS

# Check if a given string has all symbols in upper case. 
# If the string is empty or doesn't have any letter in it - function should return False.

# Input: A string (str).
# Output: A logic value (bool).

Examples:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

# Precondition: a-z, A-Z, 1-9 and spaces.

# ___________________________________________________________________________________
# SOLUTION 4. <>
def is_all_upper(text):
    if len(text) < 1:
        return False
    else:
        return text.isupper()
        
print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False

# <><><><><> Best "Clear" Solution <><><><><>
def is_all_upper(text: str) -> bool:
    return text.isupper()

# <><><><><> Best "Creative" Solution <><><><><>
is_all_upper = str.isupper

# <><><><><> Best "Speedy" Solution <><><><><>
import re

def is_all_upper(text: str) -> bool:
    return True if len(re.findall('[a-z]', text)) == 0 and len(re.findall('[A-Z]', text)) != 0 else  False

# <><><><><> Uncategorized <><><><><>
def is_all_upper(text: str) -> bool:
    return text.isupper() if text and any(char.isalpha() for char in text) else False


# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 5. 
# Is String a Number? >< 
# Checks if the string is a valid number ? 
# Elementary <>
# numbers string --
# ___________________________________________________________________________________
# Elementary
# English FR PL UK ZH-HANS

# You are given a string. 
# Your function should return True if the string is a valid number (contains digits only), 
# otherwise - False. Look at the example.

# example:
# Input: A string.
# Output: A boolean.

Examples:
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False

# How it’s used: For checking string values that must contain only digits.

# Precondition: The text contains only letters, digits and whitespace.
# ___________________________________________________________________________________
# SOLUTION 5. <>
def is_number(val: str) -> bool:
    return val.isdigit()


print("Example:")
print(is_number("34"))

# These "asserts" are used for self-checking
assert is_number("34") == True
assert is_number("df") == False
assert is_number("") == False
assert is_number("a5") == False
assert is_number("ITS A NUMBER") == False
assert is_number("5a") == False

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 6. 
# Text Formatting >< 
# Отформатируйте текст в соответствии с заданным стилем ? 
# Elementary+ <>
# Russian text --
# ___________________________________________________________________________________
# Elementary+
# EN FR PL Russian UK ZH-HANS

# Вам предоставлена длинная строка (набранная моноширинным шрифтом), 
# и вы должны разбить ее, чтобы соблюсти заданную ширину. 
# После этого вам нужно отформатировать текст в соответствии с заданным стилем: 
# - "l" означает, что вы должны выровнять текст по левому краю - left, 
# - "c" - по центру - center, 
# - "r" - по правому краю - right, 
# - а "j" означает, что вы должны выровнять текст по ширине - justify. 
# И, наконец, строки вывода не должны заканчиваться пробелами.

# Если вам нужно поместить суммарно непарное количество пробелов вокруг строки, 
# чтобы отцентрировать ее, то поставьте парное количество пробелов вперед.

# Правила выравнивания текста:

#    Поскольку мы не всегда можем поставить одинаковое количество пробелов между словами в строке, 
# поместите большие блоки пробелов сначала. Например: X---X---X--X--X--X, 
# когда вам нужно поместить 12 пробелов в 5 местах: 3-3-2-2-2.
#    Не выравнивайте последнюю строку текста.

# Вам не нужно будет разбивать слово на две части, так как предоставленной ширины вполне достаточно.

# Входные данные: Текст (строка - str), ширина (целое число - int) и стиль (строка - str).
# Выходные данные: Отформатированный текст (строка - str).

# Примеры:
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    )
    == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    )
    == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    )
    == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
)

# Предварительное условие:

# -    all(len(word) <= width for word in text.split());
# -    '\n' нету в тексте;
# -    варианты стиля в ("l", "c", "r", "j");
# -    0 < len(text) <= 1000.

# ___________________________________________________________________________________
# SOLUTION 6. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# MISSION 7. 
#  >< 
#  ? 
#  <>
#  --
# ___________________________________________________________________________________

# ___________________________________________________________________________________
# SOLUTION 7. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
