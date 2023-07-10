# Bird Language ><   
# Hello? Polly wanna cracker?
# Russian parsing string text <> 
# Elementary+ --
# ___________________________________________________________________________________
# Elementary+
# EN ES FR Russian UK

# У Стефана есть друг -- маленькая робо-птичка. 
# Какое-то время он пытался научить её говорить по-английски.
# И вот сегодня она произнесла первое слово: «hieeelalaooo». 
# Звучит как «hello», но слишком уж много гласных. 
# Стефан попросил Николу помочь с этим, и тот изучил, 
# как птица меняет слова. Теперь нам осталось только написать модуль для перевода с птичьего.

# Птичка меняет слова по следующим правилам:
# - после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
# - после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
# Гласные буквы == "aeiouy".

# Вам дана птичья фраза как несколько слов, 
# разделёных пробелами (каждая пара слов разделена одним пробелом). 
# Птичка не знает ничего о знаках пунктуации и использует только буквы.
# Все слова даны в нижнем регистре.
# Необходимо перевести эту птичью песню в понятную простым роботам фразу.

# Входные данные: Птичья фраза как строка (string).
# Выходные данные: Перевод как строка (string).

# Примеры:

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

# Связь с реальной жизнью: Этот простой «шифр» похож на тот, 
# который используют дети для своего «птичьего» языка. Но теперь-то вы легко взломаете их хитрости.

# Предусловия: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# Фраза всегда имеет перевод.
# ___________________________________________________________________________________

# SOLUTION 28. <> 
def translate(text: str) -> str:
    litters = 'aeiouy'
    translate = []
    
    while len(text) != 0:
        if text[0] not in litters and text[0] != ' ':         
            translate.append(text[0])
            text = text[2:]         
        elif text[0] in litters:
            translate.append(text[0])
            text = text[3:]           
        else:
            translate.append(text[0])
            text = text[1:]
            
    result = ''
    for el in translate:
        result += el
    
    return result


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

# <><><><><> Best "Clear" Solution <><><><><>
VOWELS = "aeiouy"

def translate(phrase):
    output = ""
    c = 0
    
    while c < len(phrase):
        output += phrase[c]
        if phrase[c] in VOWELS:
            c = c + 3
        elif phrase[c] == ' ':
            c = c + 1
        else:
            c = c + 2

    return output

# <><><><><> Best "Creative " Solution <><><><><>
import re,functools
translate=functools.partial(re.sub,r"(\w)(\1\1|.)",r"\1")

# <><><><><> Best "Speedy" Solution <><><><><>
translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])

# <><><><><> Best "3rd party" Solution <><><><><>
VOWELS = "aeiouy"

def translate(phrase):
    phrase = list(phrase)
    # print(phrase)
    for x in range(len(phrase)):
        try:
            if phrase[x] not in VOWELS and phrase[x+1] in VOWELS and phrase[x] != ' ':
                phrase.pop(x+1)
        except IndexError:
            continue    
    phrase = ''.join(phrase)
    
    for x in range(len(phrase)):
        try:
            if phrase[x] in VOWELS and phrase[x] == phrase[x+1] and phrase[x] == phrase[x+2]:
                phrase = phrase.replace(phrase[x]*3, phrase[x])
        except IndexError:
            continue
    return phrase

# <><><><><> Best "Uncategorized" Solution <><><><><>
def translate(text: str) -> str:
    for i in "aeiouy":
        text = text.replace(i+i+i, i)
    new_text = text[0]
    for i in range(1, len(text)):
        if text[i - 1] not in " aeiouy":
            new_text += ''
        else:
            new_text += text[i]
            
    return new_text

# ___________________________________________________________________________________
