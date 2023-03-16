# ___________________________________________________________________________________
# MISSION 24. 
# Three Words ><   
# How to discern words and numbers ?
# Elementary+ <> 
# Russian has-hints parsing string--
# ___________________________________________________________________________________

# Давайте научим наших роботов отличать слова от чисел.

# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.

# Примеры:
# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True

# Зачем это нужно: Эта задача подскажет вам как работать со строками и покажет некоторые полезные функции.
# Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100
# ___________________________________________________________________________________
# SOLUTION 24. <> 
def checkio(words: str) -> bool:
    count = 0
    for word in words.split():
        count = count+1 if word.isalpha() else 0
        if count == 3:
            break
    return count >= 3

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
    
# <><><><><> Best "Creative " Solution <><><><><>
checkio=lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())

checkio=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())
# <><><><><> Best "Speedy" Solution <><><><><>
import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
import re

def checkio(words: str) -> bool:
    
    # find the index of words
    # use np.diff and re to check succession
    index_gap = np.diff([i for i,w in enumerate(words.split(' ')) if w.isalpha()])
    
    index_str = ''.join([str(j) for j in index_gap])
    
    pattern = re.compile(r'11')
    
    return len(re.findall(pattern, index_str))>0


# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(words: str) -> bool:
    count: int = 0
    for word in words.split():
        if word[0].isalpha():
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False
