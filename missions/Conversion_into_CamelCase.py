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
def to_camel_case(name):
    return name.title().replace('_', '')


# <><><><><> Best "Creative" Solution <><><><><>
to_camel_case = lambda n: __import__("re").sub('\_\w', lambda m: m.group(0)[1].upper(), n.title())


# <><><><><> Best "Speedy" Solution <><><><><>
def to_camel_case(name, sep='_'):
    ans, flag = [], True
    for letter in name.lower():
        if letter == sep:
            flag = True
            continue
        ans.append(letter.upper() if flag else letter)
        flag = False
    return ''.join(ans)


# <><><><><> Uncategorized <><><><><>
def to_camel_case(name: str) -> str:
    cc = ''
    for i in name.split('_'):
        cc += i.capitalize()
    return cc


# ___________________________________________________________________________________
