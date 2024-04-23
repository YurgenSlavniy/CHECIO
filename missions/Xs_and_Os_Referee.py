# Xs and Os Referee >< 
# Referee Tic-Tac-toe game ? 
# Elementary+ <>
# Русский game has-hints matrix --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR HU JA PT-BR Русский UK ZH-HANS

# Крестики и Нолики - это игра для двух игроков (Х и О), 
# которые расставляют эти знаки на 3х3 поле. 
# Игрок, который сумел разместить три своих знака в любой горизонтали, 
# вертикали или диагонали -- выигрывает.

# Но сейчас мы не будем играть в эту игру. 
# Вы будете судить игру, и оценивать результат. 
# Вам дан результат игры, и вы должны решить, кто победил или что это ничья.
# Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
# В случае ничьи, результат должен быть "D".

# x-o-referee

# Результаты игры представлены, как список строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.

# Вх. данные: Результат игры, как список строк (unicode).
# Вых. данные: "X", "O" или "D", как строка.

# Примеры:
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

# Как это используется: Эта задача поможет вам лучше понять, 
# как работать с матрицами и вложеными массивами. 
# Ну и конечно, это будет полезно при разработке игр, 
# так как надо уметь оценивать результаты.

# Предусловия:
# - в играх может быть только один победитель или ничья;
# - len(game_result) == 3;
# - all(len(row) == 3 for row in game_result).
# ___________________________________________________________________________________
# SOLUTION <>
def checkio(game_result: list[str]) -> str:
    all_results = [game_result[0], 
                   game_result[1], 
                   game_result[2], 
                   ''.join([game_result[0][0], game_result[1][0], game_result[2][0]]), 
                   ''.join([game_result[0][1], game_result[1][1], game_result[2][1]]), 
                   ''.join([game_result[0][2], game_result[1][2], game_result[2][2]]),
                   ''.join([game_result[0][0], game_result[1][1], game_result[2][2]]),
                   ''.join([game_result[2][0], game_result[1][1], game_result[0][2]]),
                  ]
    if 'XXX' in all_results:    
        return 'X'
    elif 'OOO' in all_results:  
        return 'O'
    else:
        return 'D'

print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"


# <><><><><> Best "Clear" Solution <><><><><>
def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'


# <><><><><> Best "Creative" Solution <><><><><>
checkio=lambda r,j="".join:"DOX"[sum(m*3in[j(r[::e])[::4]for e
in(1,-1)]+r+list(map(j,zip(*r)))for m in"XOX")]


# <><><><><> Best "Speedy" Solution <><><><><>
def checkio(game_result):
    for i in range(3):
        if (game_result[i][0] in ['O', 'X']) and (game_result[i][0] == game_result[i][1] == game_result[i][2]):
            return game_result[i][0]
        if (game_result[0][i] in ['O', 'X']) and (game_result[0][i] == game_result[1][i] == game_result[2][i]):
            return game_result[0][i]
    if (game_result[1][1] in ['O', 'X']) and ((game_result[0][0] == game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] == game_result[2][0])):
        return game_result[1][1]
    return "D"
    

# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np

def checkio(game_result):
    data = np.array([d for item in game_result for d in item]).reshape(3, 3)
    all_same_mark = lambda arr: np.where(arr)[0].size > 0
    for mark in ('X', 'O'):
        if any(all_same_mark(to_check) for to_check in
               [(data == mark).all(axis=0), \
               (data == mark).all(axis=1), \
               (data.diagonal() == mark).all(axis=0), \
               (np.fliplr(data).diagonal() == mark).all(axis=0)]):
            return mark

    return 'D'
    

# <><><><><> Uncategorized <><><><><>
def checkio(game_result: list[str]) -> str:
    for i in range(len(game_result)):
        if game_result[i][0] == game_result[i][1] and game_result[i][0] == game_result[i][2]:
            if game_result[i][0].isalpha():
                return game_result[i][0]

    for i in range(len(game_result)):
        if game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            if game_result[0][i].isalpha():
                return game_result[0][i]

    if game_result[0][0] == game_result[1][1] and game_result[0][0] == game_result[2][2]:
        if game_result[0][0].isalpha():
            return game_result[0][0]
        else: 
            return 'D'

    elif game_result[0][2] == game_result[1][1] and game_result[0][2] == game_result[2][0]:
        if game_result[2][0].isalpha():
            return game_result[2][0]
        else:
            return 'D'


# ___________________________________________________________________________________
