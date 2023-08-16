# Feed Pigeons ><   
# Голуби голодны и не знают меры в еде. ?
# Simple+ <> 
# Russian has-hints logic math numbers --
# ___________________________________________________________________________________
# Simple+
# EN FR HU JA PL PT-BR Russian UK ZH-HANS

# Я начал кормить одного из голубей. Через минуту прилетело еще два, и еще через минуту прилетело еще три голубя. 
# Затем 4 и так далее (Пр: 1+2+3+4+...). Одной порции корма хватает одному голубю на минуту. 
# В случае если еды не хватает на всех птиц, то сначала едят те голуби, что прилетели ранее. 
# Голуби - это вечно голодные птицы и они будут есть и есть без остановки. 
# Если у меня есть N порций корма, то сколько голубей я смогу покормить хотя бы по разу?

# Входные данные: Количество порций корма, как целое число (int).
# Выходные данные: Количество накормленных голубей, как целое число (int).

# Примеры:
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6

# Как это используется: В этой задаче мы видим, как можно использовать программирование для моделирования ситуаций. 
# Конечно, любая модель имеет свои ограничения и приближения, но чаще всего нам и не нужна идеальная модель.

# Предусловия: 0 < N < 105.
# ___________________________________________________________________________________

# SOLUTION 29. <> 

def checkio(food: int) -> int:
    welfed_pigons = 0
    minutes = 0
    pigons = 1
    old_pigons = 0
    new_pigons = 2
     
    while food != 0:
        print(food, pigons, old_pigons, new_pigons, minutes, welfed_pigons)
        
        if food / pigons > 1:
            minutes += 1
            old_pigons = pigons
            welfed_pigons = old_pigons
            food = food - old_pigons
            pigons = old_pigons + new_pigons
            new_pigons += 1

            
        elif food / pigons == 1:
            welfed_pigons = pigons
            food = 0

        else:
            if food < welfed_pigons:
                return welfed_pigons
            else:
                welfed_pigons = welfed_pigons + (food - welfed_pigons)
                food = 0
            
    print(f'сытые голуби {welfed_pigons}, minutes {minutes}')
    return welfed_pigons


print("Example:")
print(checkio(18))

# These "asserts" are used for self-checking
assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6
assert checkio(18) == 8

# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative " Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "Uncategorized" Solution <><><><><>


# ___________________________________________________________________________________
