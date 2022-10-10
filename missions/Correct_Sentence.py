# ___________________________________________________________________________________ 
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
# SOLUTION <>
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