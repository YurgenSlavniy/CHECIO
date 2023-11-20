# ___________________________________________________________________________________
# Take and Return Argument >< 
# More usual function  ? 
# Elementary <>
# --
# ___________________________________________________________________________________
#
#  Elementary
# DE English FR PL UK ZH-HANS

# 1. Let's make our function func more usual. Let it takes some argument arg.
# 2. Return the argument value without any changes. 

# 1. Сделаем нашу функцию более привычной. Пусть требуется некоторый аргумент arg.
# 2. Вернуть значение аргумента без каких-либо изменений.
# ___________________________________________________________________________________
# SOLUTION <>
# Taken from mission Empty Function

def func(arg):
    return arg

print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True
