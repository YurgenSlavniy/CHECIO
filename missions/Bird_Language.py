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
# <><><><><> Best "Creative " Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "Uncategorized" Solution <><><><><>


# ___________________________________________________________________________________
