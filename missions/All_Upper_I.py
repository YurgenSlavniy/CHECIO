# All Upper I >< 
# Все ли символы написаны заглавными буквами ? 
# Elementary  <>
# Русский bool string --
# ___________________________________________________________________________________
# Elementary
# DE EN FR JA PL Русский UK ZH-HANS

# Проверить все ли символы в строке являются заглавными. 
# Если строка пустая или в ней нет букв - функция должна вернуть True.

# Входные данные: Строка.
# Выходные данные: Логический тип.

# Пример:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True

# Условия: a-z, A-Z, 1-9 и пробелы
# ___________________________________________________________________________________
# SOLUTION <>
def is_all_upper(text: str) -> bool:
    if text == '':
        return True    
    for el in text:
        if el.isupper() or el.isdigit() or el == ' ':
            continue  
        else:
            return False
    return True

print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
