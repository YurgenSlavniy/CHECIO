# ___________________________________________________________________________________ 
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
# SOLUTION <>
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