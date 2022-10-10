# ___________________________________________________________________________________ 
# Backward String ><   
# Reverse a string ?
# Elementary <> 
# String --
# ___________________________________________________________________________________
# Elementary
# RU JA PL English

# You should return a given string in reverse order.

# Input: A string.
# Output: A string.

# Example:
# backward_string('val') == 'lav'
# backward_string('') == ''
# backward_string('ohho') == 'ohho'
# backward_string('123456789') == '987654321'
# ___________________________________________________________________________________
# SOLUTION <>
def backward_string(val: str) -> str:
    return val[::-1]

if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
               
# <><><><><> Best "Clear" Solution  <><><><><> 
backward_string = lambda val: val[::-1]

# <><><><><> Best "Creative" Solution  <><><><><>  
backward_string=lambda s:s[::-1]

# <><><><><> "Creative"  <><><><><> 
from operator import itemgetter
backward_string = itemgetter(slice(None, None, -1))

# <><><><><> "Creative"  <><><><><>  
def backward_string(val: str) -> str:
    return "".join(x for x in val[::-1])

# <><><><><> "Creative"  <><><><><> 
def backward_string(val: str) -> str:
    val2=''
    for c in val[::-1]:
        val2 += c
    return val2
