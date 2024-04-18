# Missing Number >< 
# Найди недостающий элемент в несортированном списке арифметической прогрессии ? 
# Simple <>
# Русский int list math  --
# ___________________________________________________________________________________
# Simple
# DE EN FR PL Русский UK ZH-HANS

# Вам дана последовательность целых чисел, 
# которые являются элементами арифметической прогрессии - разница между последовательными элементами постоянна. 
# Но эта последовательность не отсортирована, и один элемент отсутствует... удачи!

# Ввод: Список целых чисел (int).
# Вывод: Целое число (int).

# Примеры:
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

# Предварительные условия:
# - длина последовательности > 2;
# - отсутствующий элемент всегда находится между двумя элементами в последовательности. 
# ___________________________________________________________________________________
# SOLUTION <>
def missing_number(items: list[int]) -> int:
    idxs = range(0, len(items) - 1)
    sort_items = sorted(items)
    steps = []
    for el in idxs:
        steps.append(sort_items[el+1] - sort_items[el])
    
    step = min(set(steps))
    start_el = sort_items[0]
    finish_el = sort_items[-1]
    
    itgrs = list(range(start_el, finish_el+1, step))
    result_digit = set(itgrs) - set(sort_items)
    for el in result_digit:
        result = int(el)
    
    return result


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
