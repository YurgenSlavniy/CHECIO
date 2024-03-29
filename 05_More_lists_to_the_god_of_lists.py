# ___________________________________________________________________________________
# MISSION 1. 
# Xs and Os Referee >< 
# Referee Tic-Tac-toe game ? 
# Moderate <>
# Russian game has-hints matrix --
# ___________________________________________________________________________________
# Крестики и Нолики - это игра для двух игроков (Х и О), 
# которые расставляют эти знаки на 3х3 поле. 
# Игрок, который сумел разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.

# Но сейчас мы не будем играть в эту игру. 
# Вы будете судить игру, и оценивать результат. 
# Вам дан результат игры, и вы должны решить, кто победил или что это ничья. 
# Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок. 
# В случае ничьи, результат должен быть "D".

# Результаты игры представлены, как список строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.

# Вх. данные: Результат игры, как список строк (unicode).
# Вых. данные: "X", "O" или "D", как строка.

# Примеры:
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

# Как это используется: Эта задача поможет вам лучше понять, 
# как работать с матрицами и вложеными массивами. Н
# у и конечно, это будет полезно при разработке игр, 
# так как надо уметь оценивать результаты.

# Предусловия:

# -    в играх может быть только один победитель или ничья;
# -    len(game_result) == 3;
# -    all(len(row) == 3 for row in game_result).

# ___________________________________________________________________________________
# SOLUTION 1. <>

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
