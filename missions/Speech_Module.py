# Speech Module ><   
# Pronouns a number by words ?
# Simple+ <> 
# Russian has-hints numbers text --
# ___________________________________________________________________________________
# Simple+
# EN FR HU JA PT-BR Russian UK ZH-HANS
# Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел.
# Для него сейчас большая проблема произносить составные числа. 
# Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу. 
# Стефан должен говорить на английском, так что вам нужно знать правила составления чисел в английском языке. 
# Все слова в строковом представлении числа должны быть разделены одним пробелом.
# Будьте осторожны с пробелами -- очень сложно увидеть двойной пробел, но это критично для компьютера.

# Вх. данные: Число, как целочисленное (int).
# Вых. данные: Текстовое написание числа, как строка (str).

# Примеры:
# assert checkio(1) == "one"
# assert checkio(2) == "two"
# assert checkio(3) == "three"
# assert checkio(4) == "four"

# Как это используется: Эта концепция будет полезна для программного обеспечения 
# по синтезу речи или автоматических систем отчетности. 
# Также это может пригодиться при написании простого бота для чата, который будет уметь составлять числа.

# Предусловия: 0 < number < 1000
# ___________________________________________________________________________________

# SOLUTION 26. <> 
import numpy as np

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    num_len = len(str(num))
    if num_len == 1:
        return FIRST_TEN[num - 1]
    
    
    elif num_len == 2:
        if num > 9 and num < 20:
            nums = np.array(range(10, 20))
            return SECOND_TEN[list(nums).index(num)]
        
        if num % 10 == 0:
            fst_smbl = str(num)[0]
            nums = np.array(range(2, 10))
            return OTHER_TENS[list(nums).index(int(fst_smbl))]
        
        
        if num >= 20 and num < 100 and not num % 10 == 0:
            first_symbol = str(num)[0]
            second_symbol = str(num)[1]
            nums_second = np.array(range(2, 10))
            return OTHER_TENS[list(nums_second).index(int(first_symbol))] + ' ' + FIRST_TEN[int(second_symbol) - 1]
            
            
    elif num_len == 3:
        first_smbl = str(num)[0]     
        second_smbl = str(num)[1:]  
        second_symb = str(num)[1]
        
        if second_symb == '0' and not num % 100 == 0:
            first_smbl = str(num)[0]
            last_smbl = str(num)[2]
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED + " " + FIRST_TEN[int(last_smbl) - 1]
        
        if num % 100 == 0:
            first_smbl = str(num)[0]
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED
        
        if num % 10 == 0 and not num % 100 == 0:
            first_smbl = str(num)[0]
            scnd_smbl = str(num)[1]
            nums = np.array(range(2, 10))    
            return FIRST_TEN[int(first_smbl) - 1] + " " + HUNDRED + " " + OTHER_TENS[list(nums).index(int(scnd_smbl))]
        
        if int(second_smbl) > 9 and int(second_smbl) < 20:
            nums = np.array(range(10, 20))
            third = SECOND_TEN[list(nums).index(int(second_smbl))]
            return FIRST_TEN[int(first_smbl) - 1] + ' ' + HUNDRED + ' ' + third
            
        
        if int(second_smbl) >= 20 and int(second_smbl) < 100:
            first_s = str(second_smbl)[0]
            second_s = str(second_smbl)[1]
            nums_second = np.array(range(2, 10))
            third = OTHER_TENS[list(nums_second).index(int(first_s))] + ' ' + FIRST_TEN[int(second_s) - 1]
            return FIRST_TEN[int(first_smbl) - 1] + ' ' + HUNDRED + ' ' + third
        

print("Example:")
print(checkio(4))

# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")


# <><><><><> Best "Clear" Solution <><><><><>
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    n = number // 100
    t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []

    n = (number // 10) % 10
    t += [OTHER_TENS[n-2]] if n > 1 else []

    n = number % (10 if n > 1 else 20)
    t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []

    return ' '.join(t)

# <><><><><> Best "Creative " Solution <><><><><>
def checkio(n, d=dict(enumerate(" one two three four five six seven eight nine ten eleven twelve".split(" ")))):
    def i(s, j=iter("o en ree ir ve f t ".split(" "))):
        for k in j: s = __import__("re").sub(k + "$", next(j), s)
        return s
    return(d[n//100]+" hundred "*(n>99)+d.get(n%100,n%100<20and i(d[n%10])+"teen"or i(d[n//10%10]).replace("u","")+"ty "+d[n%10])).strip()

# <><><><><> Best "Speedy" Solution <><><><><>
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

print(305 // 100)

def checkio(number):
    result = []
    if number >= 100:
        result.append(FIRST_TEN[number // 100] + " hundred")
    if (number % 100) // 10 > 1:
        result.append(OTHER_TENS[((number % 100) // 10) - 2])
    if (number % 100) // 10 == 1:
        result.append(SECOND_TEN[number % 10])
    elif (number % 10) > 0:
        result.append(FIRST_TEN[number % 10])
        
    return ' '.join(result)


# <><><><><> Best "Uncategorized" Solution <><><><><>
def checkio(num: int) -> str:
    if num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 9:
        return 'nine'
    elif num == 10:
        return 'ten'
    elif num == 11:
        return 'eleven'
    elif num == 12:
        return 'twelve'
    elif num == 13:
        return 'thirteen'
    elif num == 14:
        return 'fourteen'
    elif num == 15:
        return 'fifteen'
    elif num == 16:
        return 'sixteen'
    elif num == 17:
        return 'seventeen'
    elif num == 18:
        return 'eighteen'
    elif num == 19:
        return 'nineteen'
    elif num == 999:
        return 'nine hundred ninety nine'
    elif num == 784:
        return 'seven hundred eighty four'
    elif num == 777:
        return 'seven hundred seventy seven'
    elif num == 88:
        return 'eighty eight'
    elif num == 44:
        return 'forty four'
    elif num == 20:
        return 'twenty'
    elif num == 30:
        return 'thirty'
    elif num == 40:
        return 'forty'
    elif num == 50:
        return 'fifty'
    elif num == 80:
        return 'eighty'
    elif num == 90:
        return 'ninety'
    elif num == 100:
        return 'one hundred'
    elif num == 200:
        return 'two hundred'
    elif num == 300:
        return 'three hundred'
    elif num == 600:
        return 'six hundred'
    elif num == 700:
        return 'seven hundred'
    elif num == 900:
        return 'nine hundred'
    elif num == 21:
        return 'twenty one'
    elif num == 312:
        return 'three hundred twelve'
    elif num == 302:
        return 'three hundred two'
    elif num == 509:
        return 'five hundred nine'
    elif num == 753:
        return 'seven hundred fifty three'
    elif num == 940:
        return 'nine hundred forty'
    elif num == 999:
        return 'nine hundred ninety nine'
    elif num == 98:
        return 'ninety eight'
    elif num == 55:
        return 'fifty five'
    elif num == 23:
        return 'twenty three'
    elif num == 100:
        return 'one hundred'
    elif num == 761:
        return 'seven hundred sixty one'
    elif num == 637:
        return 'six hundred thirty seven'
    elif num == 856:
        return 'eight hundred fifty six'
    elif num == 742:
        return 'seven hundred forty two'
    elif num == 592:
        return 'five hundred ninety two'
    elif num == 269:
        return 'two hundred sixty nine'

# ___________________________________________________________________________________

