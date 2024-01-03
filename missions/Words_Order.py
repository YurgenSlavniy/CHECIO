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
def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

# <><><><><> Best "Creative" Solution <><><><><>
import re

def words_order(text, words):
    return len(set(words)) == len(words) and \
        not not re.search(r'\b' + r'\b.*\b'.join(words) + r'\b', text)

# <><><><><> Best "Speedy" Solution <><><><><>
def words_order(text: str, words: list) -> bool:
    # A word that appears twice make this simple.
    if len(set(words)) != len(words):
        return False
    # Look for words indexes with a simple iteration on text words.
    words = {word: -1 for word in words}  # A dict remembers insertion order.
    for n, text_word in enumerate(text.split()):
        if text_word in words and words[text_word] == -1:
            words[text_word] = n
    # Make sure all words are in the text and indexes are increasing.
    last = -1
    for index in words.values():
        if index <= last:
            return False
        last = index
    return True

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def words_order(text: str, words: list) -> bool:

    text_split = text.split(" ")
    lg = len(words)
    
    count_list = np.array([text_split.count(x) for x in words])
    # print(count_list)
    if np.sum(count_list != 0) == lg:
        index_list = np.array([text_split.index(x) for x in words])
        # print(index_list)
        return np.sum(index_list == np.sort(index_list)) == lg\
            and len(np.unique(index_list)) == lg            
    else:
        return False

# <><><><><> Uncategorized <><><><><>
def words_order(text: str, words: list) -> bool:
    without_duplicate = list(set(words))
    if len(without_duplicate) != len(words):
        return False

    list_text = text.split(" ")

    unique_list = []

    for item in list_text:
        if item not in unique_list and item in words:
            unique_list.append(item)

    return unique_list == words
