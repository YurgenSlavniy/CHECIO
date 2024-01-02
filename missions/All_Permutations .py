# All Permutations>< 
# Show me every permutation!  ? 
# Undefined <>
# math string  --
# ___________________________________________________________________________________
# Undefined
# English

# Given a string, return all possible permutations of its characters, sorted alphabetically.

# example
# Input: String (str).
# Output: Iterable of strings (str).

# Examples:
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

# How it’s used:
# - puzzles and games like Scrabble where word combinations matter;
# - cryptography to test possible keys given a set of characters;
# - data analysis in genetics for possible gene combinations.

# ___________________________________________________________________________________
# SOLUTION <>
# Для решения этой задачи мы можем использовать рекурсию. 
# Мы начинаем с пустой строки и добавляем по одному символу из исходной 
# строки до тех пор, пока не получим строку, длиной равной исходной строке.
# При каждом шаге мы проверяем, что символ еще не был использован в текущей комбинации,
# и если он не был использован, то добавляем его к текущей комбинации 
# и вызываем функцию рекурсивно для оставшихся символов. 
#  Когда мы получаем строку, длиной равной исходной строке, 
# мы добавляем ее в список результатов.
from collections.abc import Iterable
import itertools

def string_permutations(s: str) -> list:
    results = []
    used = [False] * len(s)
    
    def backtrack(combination):
        if len(combination) == len(s):
            results.append(combination)
            return
        
        for i in range(len(s)):
            if used[i]:
                continue
            used[i] = True
            backtrack(combination + s[i])
            used[i] = False
    
    backtrack("")
    return sorted(results)


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

# Мы начинаем с пустой строки и списком used, 
# который содержит флаги для каждого символа в строке, указывающие, 
# был ли символ использован в текущей комбинации. 
# Затем мы определяем функцию backtrack, которая будет вызываться рекурсивно.

# В функции backtrack мы проверяем, 
# что длина текущей комбинации равна длине исходной строки.
# Если это так, то мы добавляем текущую комбинацию в список результатов 
# и возвращаемся из функции.

# Если текущая комбинация не является полной, 
# то мы проходим по всем символам в строке и проверяем, 
# был ли символ уже использован в текущей комбинации. 
# Если символ уже был использован, то мы пропускаем его. 
# Если символ еще не был использован, 
# то мы добавляем его к текущей комбинации, 
# устанавливаем флаг использования символа в списке used 
# и вызываем функцию backtrack рекурсивно для оставшихся символов. 
# После этого мы снимаем флаг использования символа из списка used 
# и удаляем добавленный символ из текущей комбинации.

# В конце мы вызываем функцию backtrack с пустой строкой 
# и возвращаем отсортированный список результатов.

# <><><><><> Best "Clear" Solution <><><><><>

# <><><><><> Best "Creative" Solution <><><><><>

# <><><><><> Best "Speedy" Solution <><><><><>

# <><><><><> Best "3rd party" Solution <><><><><>

# <><><><><> Uncategorized <><><><><>

# ___________________________________________________________________________________
