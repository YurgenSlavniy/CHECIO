# ___________________________________________________________________________________
# Longest Substring of Unique Characters >< 
# Longest sequence of distinct characters? 
# Undefined <>
# string --
# ___________________________________________________________________________________
# Undefined
# DE English FR PL UK ZH-HANS

# Given a string, find the length of the longest substring without repeating characters.

# example
# Input: String (str).
# Output: Integer (int).

# Examples:
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6

# How it’s used:

# -    data validation for passwords to ensure the inclusion of a sufficiently long sequence of non-repeated characters;
# -    text analysis, especially for cryptography and coding patterns;
# -    identifying unique patterns in a sequence.
# ___________________________________________________________________________________
# SOLUTION <>
def longest_substr(s: str) -> int:
        
    if len(s) < 1:
        return 0
    else:
        # Получаем длину строки
        n = len(s)
        # Создаем множество для хранения уникальных символов в текущей подстроке
        char_set = set()
        # Инициализируем переменные для ответа, начала и конца текущей подстроки
        ans, i, j = 0, 0, 0
        # Итерируемся по строке, пока не достигнем конца строки
        while i < n and j < n:
            # Если текущий символ еще не встречался в текущей подстроке
            if s[j] not in char_set:
                # Добавляем его в множество уникальных символов
                char_set.add(s[j])
                # Увеличиваем конец текущей подстроки
                j += 1
                # Обновляем ответ, если текущая подстрока больше предыдущей
                ans = max(ans, j - i)
            # Если текущий символ уже был в текущей подстроке
            else:
                # Удаляем первый символ из текущей подстроки
                char_set.remove(s[i])
                # Увеличиваем начало текущей подстроки
                i += 1
        # Возвращаем длину самой длинной подстроки без повторяющихся символов
        return ans

        # Получаем длину строки
        n = len(s)
        # Создаем множество для хранения уникальных символов в текущей подстроке
        char_set = set()
        # Инициализируем переменные для ответа, начала и конца текущей подстроки
        ans, i, j = 0, 0, 0
        # Итерируемся по строке, пока не достигнем конца строки
        while i < n and j < n:
            # Если текущий символ еще не встречался в текущей подстроке
            if s[j] not in char_set:
                # Добавляем его в множество уникальных символов
                char_set.add(s[j])
                # Увеличиваем конец текущей подстроки
                j += 1
                # Обновляем ответ, если текущая подстрока больше предыдущей
                ans = max(ans, j - i)
            # Если текущий символ уже был в текущей подстроке
            else:
                # Удаляем первый символ из текущей подстроки
                char_set.remove(s[i])
                # Увеличиваем начало текущей подстроки
                i += 1
        # Возвращаем длину самой длинной подстроки без повторяющихся символов
        return ans

print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3
