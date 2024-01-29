# Armstrong Number Checking >< 
# Narcissistic number ? 
# Undefined <>
# bool math numbers --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# In number theory, an Armstrong number (after Michael F. Armstrong) 
# or narcissistic number in a given number base 
# (10 for this mission) is a number that is the sum of 
# its own digits each raised to the power of the number of digits.
# For example, 153 is an Armstrong number because 13 + 53 + 33 == 153.

# Input: Integer (int).
# Output: Logic value (bool).

# Examples:
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True

# How it’s used: 
# - this function can be employed in mathematical puzzles, 
# encryption algorithms, and educational tools.  

# ___________________________________________________________________________________
# SOLUTION <>
def is_armstrong(num: int) -> bool:
    len_num = len(str(num)) 
    armstrong_sum = sum(int(digit)**len_num for digit in str(num))
    return armstrong_sum == num


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

# <><><><><> Best "Clear" Solution <><><><><>
def is_armstrong(num: int) -> bool:
    
    temp, digits, count = num,  [], 0
    while temp:
        temp, digit = divmod(temp, 10)
        digits.append(digit)
        count += 1

    return sum(d**count for d in digits) == num

# <><><><><> Best "Creative" Solution <><><><><>
is_armstrong = lambda num: num == sum(map(lambda x: x**len(str(num)),map(int,str(num))))

# <><><><><> Best "Speedy" Solution <><><><><>
def is_armstrong(num: int) -> bool:
    return sum([int(i)**len(str(num)) for i in str(num)]) == num

# <><><><><> Uncategorized <><><><><>
def is_armstrong(num: int) -> bool:
    # your code here
    text = str(num)
    l = len(text)
    res = 0
    for digit in text:
        res += int(digit) ** l
        
    return res == num

# ___________________________________________________________________________________
