# ___________________________________________________________________________________ 
# Right to Left >< 
# “Left, right, left, right, left, left, left. Your destination is on the left.” “Wait, this isn’t where I was going…” ? 
# Elementary <>
# Russian string parsing has-Hints --
# ___________________________________________________________________________________
#  Elementary
# PL DE JA Russian UK EN ES IT EL FR

# "На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
# Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
# "Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"."
# Scientific American. www.scientificamerican.com

# Один робот был занят простой задачей: 
# объединить последовательность строк в одно выражение для создания инструкции по обходу корабля. 
# Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
# Дана последовательность строк. Вы должны объединить эти строки в блок текста, 
# разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, 
# вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

# Входные данные: Последовательность строк.
# Выходные данные: Текст, как строка.

# Пример:
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"

# Как это используется: Это просто пример операций, использующих строки и последовательности.
# Предусловие:
# 0 < len(phrases) < 42
# ___________________________________________________________________________________
# SOLUTION <>
def left_join(message_text):
    join_mess = ','.join(message_text)
    replace = join_mess.replace('right', 'left')
    return replace


print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

# <><><><><> Best "Clear" Solution <><><><><>
def left_join(phrases):
    return (",".join(phrases)).replace("right","left")

# <><><><><> Best "Creative" Solution <><><><><>
def left_join(phrases):
    return ','.join(map(lambda x:x.replace('right','left'),phrases))

# <><><><><> Best "Speedy" Solution <><><><><>
def left_join(phrases):
    return ",".join(phrases).replace("right", "left")

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

class right_to_left():
    def __init__(self, phrases):
        self.phrases = phrases

    def perform(self):
        replaced_words_array = np.array([p.replace('right', 'left') for p in self.phrases])
        replaced_words_list = replaced_words_array.tolist()
        return ",".join(replaced_words_list)

def left_join(phrases: tuple) -> str:
    foo = right_to_left(phrases)
    return foo.perform()

# <><><><><> "Creative" Solution <><><><><>
def left_join(phrases):
    a=""
    for i in phrases:
        a=a+","+i
    a=a[1:].replace("right", "left")
    return a