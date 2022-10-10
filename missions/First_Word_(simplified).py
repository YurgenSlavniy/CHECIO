# ___________________________________________________________________________________ 
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
# SOLUTION <>

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
