# The Most Wanted Letter >< 
# Find out which is the most wanted letter ? 
# Elementary+ <>
# Русский has-hints statistics string --
# ___________________________________________________________________________________
# Elementary+
# DE EL EN ES FR HU JA PL PT-BR Русский UK ZH-HANS

# Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте.
# Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, 
# так что при подсчете считайте, что "A" == "a". 
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.


# Если в тексте две и больше буквы с одинаковой частотой, 
# тогда результатом будет буква, которая идет первой в алфавите. 
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

# Вх. данные: Текст для анализа, как строка.
# Вых. данные: Наиболее частая буква, как строка.

# Примеры:
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"

# Как это используется: Для большинства задач по дешифрованию необходимо 
# знать частоту появления различных букв в подобном тексте. 
# Для примера, мы легко можем взломать одноалфавитный шифр подстановки,
# если мы знаем вероятность появления букв. Это также может быть полезной информацией для лингвистов.

# Предусловия:
# text содержит только ASCII символы.
# 0 < len(text) ≤ 105  
# ___________________________________________________________________________________
# SOLUTION <>
def checkio(text: str) -> str:
    text = text.lower()
    litters = []
    for el in text:
        if el.isalpha():
            litters.append(el)
    litters_sort_set = sorted(set(litters))   
    litters_count = {}
    for el in litters_sort_set:
        litters_count[el] = text.count(el)
       
    return max(litters_count, key=litters_count.get)
        

print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"
# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
