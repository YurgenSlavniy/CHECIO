# ___________________________________________________________________________________
# Correct Capital >< 
# Check whether the register is used correctly. ? 
# Elementary+ <>
# bool logic string --
# ___________________________________________________________________________________
#  Elementary+
# English UK

# You are given a word in which letters can be in different cases. 
# Your task is to check whether the case was used correctly in the line. 
# If everything is correct - return True, if there are errors - return return False.

# Examples of the correct use of cases:

# All characters in the string are in uppercase. For example, "CHECKIO";
# None of the characters are in uppercase. For example, "checkio";
# Only the first character is in uppercase. For example, "Checkio".

# Вам дается слово, в котором буквы могут быть в разных падежах.
# Ваша задача - проверить, правильно ли был использован регистр в строке. 
# Если все правильно - верните True, если есть ошибки - верните return False.

# Примеры правильного использования падежей:

# Все символы в строке набраны в верхнем регистре. Например, "CHECKIO";
# Ни один из символов не написан заглавными буквами. Например, "checkio";
# В верхнем регистре указан только первый символ. Например, "Checkio".

# Input: String.
# Output: Bool.

# Examples:

assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True
# ___________________________________________________________________________________

# SOLUTION 2. <>
def correct_capital(line: str) -> bool:
    c1 = line[0].isupper()
    c2 = line[1:].isupper()
    c3 = line[1:].islower()
    c4 = line.islower()
    
    return (c1 and c2) or (c1 and c3) or c4

print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

# <><><><><> Best "Clear" Solution <><><><><>
correct_capital = lambda s: s in {s.upper(), s.lower(), s.capitalize()}

# <><><><><> Best "Creative" Solution <><><><><>
correct_capital = lambda line: line in (line.capitalize(), line.upper(), line.lower())

# <><><><><> Best "Speedy" Solution <><><><><>
import re
from string import ascii_lowercase, ascii_uppercase

_l = rf'[{ascii_lowercase}]'
_u = rf'[{ascii_uppercase}]'
incorrect = re.compile(rf'({_l}{_u})|(\b{_u}{{2,}}{_l})')

def correct_capital(line: str) -> bool:
    return not incorrect.search(line)
    
# <><><><><> Uncategorized <><><><><>
def correct_capital(line: str) -> bool:
    # your code here
    return any ([line == line.upper(), line ==line.lower(), line==line[0]+line[1:].lower()])

# ___________________________________________________________________________________

