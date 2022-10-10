# ___________________________________________________________________________________
# Acceptable Password I >< 
# длина строки должна быть больше 6 ? 
# Elementary <>
# Russian string Bool --
# ___________________________________________________________________________________
# Elementary
# EN Russian JA PL

# Вы начали серию задач связаную с паролями. Каждая следующая задача связана с предыдущей. 
# Каждая следующая задача будет сложнее предыдущей.
# В этой задаче, Вам нужно создать функцию проверки пароля.
# Условия проверки:
# длина пароля должна быть больше 6.

# Входные данные: Строка.
# Выходные данные: Логический тип.

# Пример:
# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == True

# Для чего это нужно: Для проверки заполнения пароля. Кроме того, полезно будет научиться оценивать задачи.
# ___________________________________________________________________________________
# SOLUTION <>

def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False
    else:
        return True
      
if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    
# <><><><><> Best "Clear" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6

# <><><><><> Best "Creative" Solution <><><><><>
def is_acceptable_password(password: str) -> bool:
    return bool(password[7::])

# <><><><><> Clear solution <><><><><>
is_acceptable_password = lambda password: len(password) > 6

# <><><><><> Uncategorized solution <><><><><>
def is_acceptable_password(password: str) -> bool: 
    return True if len(password) > 6 else False 
