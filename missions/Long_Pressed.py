# Long Pressed >< 
# Check the loooooooong-pressed letter ? 
# Simple <>
# encode-decode string --
# ___________________________________________________________________________________
#  Simple
# DE English FR PL UK ZH-HANS

# "I Love you soooooo much! You are the best!!"

# Sometimes your friends want to express their feelings in a message, 
# and sometimes a key with a letter gets stuck on the keyboard. 
# In both cases we will get a "long-pressed letter" 
# and the letter will then be printed more than once. 
# You are given two strings. The first string is the original text message. 
# The second string is a printed message, 
# which may contain several (or possibly none) long-pressed letters. 
# It may happen that the message was written in a hurry, 
# so do not forget to check that all the letters match those in the original. 
# Return True if the printed message matches the original one, 
# taking into account possible long keystrokes. 
# Or False if there are errors or no long-pressed letters.

# Input: String (str).
# Output: Logic value (bool).

# Examples:
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False

# Preconditions:
# - "text" and "typed" consist of only lowercase English letters and symbols "'/?!.,;    
# - 1 <= len(text), len(typed) <= 1000.
# ___________________________________________________________________________________
# SOLUTION <>
def long_pressed(text: str, typed: str) -> bool:
        
    if len(text.split(' ')) == len(typed.split(' ')):
        results = []
        for el in range(0, len(text.split(' '))):
            if len(text.split(' ')[el]) == len(typed.split(' ')[el]) and text.split(' ')[el] == typed.split(' ')[el]:
                results.append(False)                
            elif len(text.split(' ')[el]) == len(typed.split(' ')[el]) and text.split(' ')[el] != typed.split(' ')[el]:
                return False                
            elif len(text.split(' ')[el]) != len(typed.split(' ')[el]):
                if set(text.split(' ')[el]) == set(typed.split(' ')[el]):
                    results.append(True)
                else:
                    return False
    else:
        return False
    
    if True in results:
        return True
    else:
        return False


print("Example:")
print(long_pressed("alex", "aaleex"))


# These "asserts" are used for self-checking
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
