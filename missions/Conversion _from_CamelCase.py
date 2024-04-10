# Conversion from CamelCase >< 
# Преобразуйте строку из CamelCase в under_score ? 
# Elementary+ <>
# Русский string text --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR PL Русский UK ZH-HANS

# Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) 
# из формата CamelCase, принятого в JavaScript (MyFunctionName) в формат, 
# принятый в Python (my_function_name), 
# где все буквы - маленькие, а слова соединены знаком нижнего подчеркивания "_".

# Входные данные: Название функции как строка в CamelCase
# Output: То же самое название, но в under_score

# Примеры:
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

# Как это используется: Чтобы применять названия функций в том стиле, 
# в каком они приняты в определенном языке (Python, JavaScript, и т.д.).

# Предусловия:
# 0 < len(string) <= 100
# Во входящих данных не будет чисел или пустых строк
# ___________________________________________________________________________________
# SOLUTION <>
def from_camel_case(name: str) -> str:
    result = []
    result.append(name[0].lower())
    for el in name[1:]:
        if el.isupper():
            result.append('_')
            result.append(el.lower())
        else:
            result.append(el)
    
    return ''.join(result)


print("Example:")
print(from_camel_case("MyFunctionName"))

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
