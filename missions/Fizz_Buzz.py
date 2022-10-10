# ___________________________________________________________________________________ 
# Fizz Buzz ><   
# A word game used to the teach robots about division?
# Elementary <> 
# String numbers has-Hints Bool --
# ___________________________________________________________________________________
# Elementary
# ES JA ZH-CN ZH-HANS EN EL FA HU IT PL Russian UK CS DE FR PT-BR

# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

# Вы должны написать функцию, которая принимает положительное целое число и возвращает:
# "Fizz Buzz" , если число делится на 3 и 5;
# "Fizz" , если число делится на 3;
# "Buzz" , если число делится на 5;
# Число , как строку для остальных случаев.

# Входные данные: Число, как целочисленное (int).
# Выходные данные: Ответ, как строка (str).

# Примеры:
# checkio(15) == "Fizz Buzz"
# checkio(6) == "Fizz"
# checkio(5) == "Buzz"
# checkio(7) == "7"

# Как это используется: Здесь вы можете научиться как писать простейшую функцию и работать с if-else.

# Предусловия: 0 < number ≤ 1000
# ___________________________________________________________________________________
# SOLUTION <>

# Your optional code here
# You can import some modules or create additional functions
def checkio(number: int) -> str:
    if number % 5 == 0 and number % 3 == 0:
        return "Fizz Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)
# Some hints:
# Convert a number in the string with str(n)
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
               
# <><><><><> Best "Creative" Solution  <><><><><>               
checkio=lambda n:("Fizz "*(1-n%3)+"Buzz "*(1-n%5))[:-1]or str(n)

# <><><><><> Best "Speedy" Solution <><><><><>  
def checkio(number):
    if number % 3 == 0:
        result = 'Fizz'
        if number % 5 == 0:
            result += ' Buzz'
    elif number % 5 == 0:
        result = 'Buzz'
    else:
        result = s
    return result

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def checkio(a):
    if (np.mod(a,5)==0)&(np.mod(a,3)==0):
        n="Fizz Buzz"
        print('lol')
    elif np.mod(a,3)==0:
        n="Fizz"
    elif np.mod(a,5)==0:
        n="Buzz"
    else:
        n=str(a)
    return n

# <><><><><> Best "Scary" Solution <><><><><> 
ghostbuster = str

def checkio(number):
    scary_number = 1 * number
    
    woo = not scary_number % 5
    boo = not scary_number % 3
    
    if woo and boo:
        return "Fizz Buzz"
    if woo:
        return "Buzz"
    if boo:
        return "Fizz"
    return ghostbuster(scary_number)
