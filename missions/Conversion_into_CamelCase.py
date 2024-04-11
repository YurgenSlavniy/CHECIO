# Conversion into CamelCase >< 
# Преобразуйте строку в CamelCase ? 
# Elementary+ <>
# Русский string text --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR PL Русский UK ZH-HANS

# Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) 
# из формата, принятого в Python (my_function_name) в CamelCase, 
# принятый в JavaScript (MyFunctionName), где первая буква каждого слова - большая/заглавная.

# Входные данные: Название функции как строка
# Output: То же самое название, но в CamelCase

# Примеры:
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

# Как это используется: Чтобы применять названия функций в том стиле, 
# в каком они приняты в определенном языке (Python, JavaScript, и т.д.).

# Предусловия:
# 0 < len(string) <= 100
# Во входящих данных не будет чисел или пустых строк 
# ___________________________________________________________________________________
# SOLUTION <>
def to_camel_case(name: str) -> str:
    split = name.split('_')
    split = [item.capitalize() for item in split]
    return ''.join(split)
        
print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________