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
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
