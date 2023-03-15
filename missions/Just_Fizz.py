# ___________________________________________________________________________________
# MISSION 18. 
# Just Fizz! ><   
# Check divisible by 3 as...1, 2, Fizz! ?
# Elementary+  <> 
# bool numbers string --
# ___________________________________________________________________________________
# Elementary+
# English UK

# The mission is in Blocked Mode. Access to the solutions is blocked for a day or two (even after you share your own), 
# until we'll have enough solutions for you to check. All users who've solved the mission will get the notifications about their opening.
# juggler
# This is a simplified version of Fizz Buzz mission.

# You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible by 3 (3, 6, 9 ...) 
# otherwise convert the given number to a string (2 -> "2").

# Input: An integer.
# Output: String.

# Examples:
# assert checkio(15) == "Fizz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "10"
# assert checkio(7) == "7"
# ___________________________________________________________________________________
# SOLUTION 18. <>
def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

# <><><><><> Best "Clear" Solution <><><><><>
def checkio(num: int) -> str:
    return str(num) if num % 3 else 'Fizz'

# <><><><><> Best "Creative " Solution <><><><><>
checkio = lambda v: 'Fizz' if v % 3 == 0 else str(v)

# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(num: int) -> str:
    # your code here
    return "Fizz" if num%3==0 else str(num)

# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 6 == 0:
        return "Fizz"
    else:
        return str(num)
    return ""
