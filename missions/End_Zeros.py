# ___________________________________________________________________________________ 
# End Zeros ><   
# How many zeros are at the end?
# Elementary <> 
# String --
# ___________________________________________________________________________________
# Elementary
# EN JA PL Russian

# Попробуйте выяснить какое количество нулей содержит данное число в конце.

# Входные данные: Положительное целое число (int).
# Выходные данные: Целое число (int).

# Пример:
# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0
# ___________________________________________________________________________________
# SOLUTION <>
def end_zeros(num: int) -> int:
    num_str = str(num)
    num_str = num_str[::-1] # инвертирование нулями вперёд
    count = 0

    for i in num_str:
        if i=='0':
            count+=1
        else:
            break
    return count


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2        
    
# <><><><><> Best "Clear" Solution <><><><><>   
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))

# <><><><><> Best "Creative" Solution  <><><><><>  
def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if  x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))

# <><><><><> Best "Speedy" Solution <><><><><>    
def end_zeros(num: int) -> int:
    # your code here
    if num == 0:
        return 1
    
    zeros = 0
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros

# <><><><><> Best "3rd party" Solution <><><><><> 
import numpy as np

def end_zeros(b):
    if b==0:
        return 1
    for i in np.arange(1,len(str(b))+1):
        if float(b/(10**i)).is_integer()==False:
            break
    return i-1
