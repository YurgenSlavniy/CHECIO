# ___________________________________________________________________________________ 
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
# SOLUTION <>
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
