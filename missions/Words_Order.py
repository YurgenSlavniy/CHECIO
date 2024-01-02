# Words Order >< 
# Check that the words are given in the correct order ? 
# Elementary+  <>
# list string  --
# ___________________________________________________________________________________
# Elementary+
# English

# You have a text and a sequence of words. 
# You need to check if the words in sequence appear in the same order as in the given text.

# Cases you should expect while solving this challenge:

#    a word from the sequence is not in the text - your function should return False;
#    any word can appear more than once in a text - use only the first one;
#    two words in the given sequence are the same - your function should return False;
#    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
#    the text includes only English letters and spaces.

# Input: Two arguments. The first one is a given text as a string (str), the second is list of words as strings (str).
# Output: Logic value (bool).

# Examples:
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
# ___________________________________________________________________________________
# SOLUTION <>
# Для решения этой задачи мы можем использовать метод split() 
# для разделения строки text на список слов и затем проверить, 
# что все слова из списка words присутствуют в этом списке слов и в правильном порядке. 
# Если какое-то слово отсутствует или они идут в неправильном порядке, 
# то мы возвращаем False. 
# Если все слова присутствуют и идут в правильном порядке, то мы возвращаем True.

def words_order(text: str, words: list) -> bool:
    text_words = text.split()
    last_index = -1
    for word in words:
        if word not in text_words:
            return False
        index = text_words.index(word)
        if index <= last_index:
            return False
        last_index = index
    return True

print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

# Мы начинаем с разделения строки text на список слов text_words. 
# Затем мы проходим по каждому слову из списка words и проверяем, 
# что оно присутствует в списке text_words и идет после предыдущего слова
# (если оно есть). 
# Если какое-то слово отсутствует или идет перед предыдущим словом, 
# то мы возвращаем False. 
# Если все слова присутствуют и идут в правильном порядке,
# то мы возвращаем True.

# <><><><><> Best "Clear" Solution <><><><><>

# <><><><><> Best "Creative" Solution <><><><><>

# <><><><><> Best "Speedy" Solution <><><><><>

# <><><><><> Best "3rd party" Solution <><><><><>

# <><><><><> Uncategorized <><><><><>
