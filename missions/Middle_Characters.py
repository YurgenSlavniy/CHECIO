# Middle Characters >< 
# Найди символ(ы) в середине строки ? 
# Elementary+ <>
# Русский parsing string text --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR PL Русский UK ZH-HANS

# У вас есть определенная строка, в которой вы хотите найти средние символы. 
# Строка может состоять как из одного слова или даже нескольких символов, 
# так и быть целым предложением. Если длина строки четная - 
# вам необходимо вернуть два средних символа, если же нечетная - только один. 
# Более наглядно это описано в Примерах.

# Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Median.

# Входные данные: Строка.
# Выходные данные: Средние символы.

# Примеры:
assert middle("example") == "m"
assert middle("test") == "es"

# Как это используется: для работы с текстами.
# Предусловие: 1 <= длина строки <= 100/
# ___________________________________________________________________________________
# SOLUTION <>
def middle(text: str) -> str:
    if len(text) %2 == 0:        
        return text[int((len(text)/2)-1):int((len(text)/2)+1)]
    else:
        return text[int(len(text)/2)]
        
        
print("Example:")
print(middle("example"))

assert middle("example") == "m"
assert middle("test") == "es"


# <><><><><> Best "Clear" Solution <><><><><>
def middle(text):
    n = len(text) // 2 + 1
    return text[-n:n]


# <><><><><> Best "Creative" Solution <><><><><>
def middle(text):
    n = len(text) // 2
    return text[~n:n+1]


# <><><><><> Best "Speedy" Solution <><><><><>
def middle(text):
    #replace this for solution
    return (text[(len(text)-1)//2:(len(text)-1)//2*-1] or text)


# <><><><><> Uncategorized <><><><><>
def middle(text: str) -> str:

    ind, rem = divmod(len(text), 2)
    result = text[ind+rem-1: ind+1]
        
    return result


# ___________________________________________________________________________________
