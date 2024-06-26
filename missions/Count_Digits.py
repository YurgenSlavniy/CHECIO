# Count Digits >< 
# Вам нужно подсчитать количество цифр в данной строке ? 
# Elementary <>
# numbers string --
# ___________________________________________________________________________________
# Elementary

# Вам нужно подсчитать количество цифр в данной строке.

# Входные данные: строка.
# Выходные данные: целое число.

# Примеры:
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)
 

# ___________________________________________________________________________________
# SOLUTION <>
def count_digits(text: str) -> int:
  
    integers = []
    for el in text:
        if el.isdigit():
            integers.append(el)
    return len(integers)


print("Example:")
print(count_digits("hi"))

# These "asserts" are used for self-checking
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)
assert count_digits("5 plus 6 is") == 2
assert count_digits("") == 0


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
