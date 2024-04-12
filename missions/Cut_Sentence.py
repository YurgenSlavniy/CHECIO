# Cut Sentence >< 
# Урежьте предложение так, чтобы оно было короче или равно заданной длине. ? 
# Russian has-hints string text <>
# Elementary+ --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR PL Russian UK ZH-HANS

# В этой миссии Ваша задача состоит в том, 
# чтобы урезать предложение до длины, 
# которая не превышает заданное количество символов.

# Если данное предложение уже достаточно короткое, 
# Вам не нужно ничего с ним делать. В случае, если его нужно урезать, 
# отсутствующая часть должна быть обозначена присоединением многоточия ("...") 
# к концу сокращенного предложения.

# Сокращенное предложение может содержать целые слова и пробелы.
# Оно не должно содержать ни усеченных слов, ни конечных пробелов.
# Многоточие было учтено при расчете разрешенного количества символов, поэтому оно не засчитывается в счет заданной длины.

# example
# Входные данные: Два аргумента:
# - однострочное предложение в виде str;
# - максимальная длина усеченного предложения в виде int.
# Выходные данные: Урезанное предложение с многоточием (если требуется) в виде одной строки.

# Примеры:
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

# Предварительное условие:

# -   line.startswith(' ') == False
# -   0 < len(line) ≤ 79
# -   0 < length ≤ 76
# -   all(char in string.ascii_letters + ' ' for char in line)
 
# ___________________________________________________________________________________
# SOLUTION <>
def cut_sentence(line: str, length: int) -> str:
    if len(line) <= length:
        return line
    else:
        new_line = line[:length]
        split_line = line.split(' ')
        new_line_split = new_line.split(' ')
        result_line = []
        idx = len(new_line_split)
        for el in range(0, idx):
            if split_line[el] == new_line_split[el]:
                result_line.append(split_line[el])
        
        return ' '.join(result_line) + '...'

print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
