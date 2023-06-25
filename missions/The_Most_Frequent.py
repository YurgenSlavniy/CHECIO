# The Most Frequent >< 
# Определите наиболее часто встречающийся элемент в последовательности. ? 
# Elementary <>
# Russian has-hints list statistics --
# ___________________________________________________________________________________
# Elementary
# EN JA Russian UK ZH-HANS
# Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.

# Входные данные: список строк.
# Выходные данные: строка.

# Примеры:
# assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
# assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

# ___________________________________________________________________________________
# SOLUTION 19. <>
def most_frequent(data: list[str]) -> str:
    return max(set(data), key=data.count)
    
print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
