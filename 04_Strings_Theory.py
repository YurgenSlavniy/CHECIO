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

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
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

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
