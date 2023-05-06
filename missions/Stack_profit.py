# Stock Profit >< 
# Find the best time to buy and the best time to sell ? 
# Elementary+ <>
# game list --
# ___________________________________________________________________________________
# You are a broker on the stock exchange. 
# You've decided to make just one complete operation: 
# to buy a stock and sell it later to make a profit. 
# “Short-selling” (sell first, buy later) is not allowed in this market.

# Buying and selling prices for every distinct moment are the same 
# (in every moment you may either by a stock for price x or sell a stock 
# (if you have it) for the same price x) and are shown in the given list stock.

# So, you have to choose, what are the best prices to buy a stock and later sell
# it to make the maximum profit from the operation.
# Your function must return this maximum possible profit. 
# If it's not possible to make any profit with given prices (it's <= 0), your function should return 0.

# Input: Stock prices as list of integers.
# Output: Maximum possible profit as integer.

# Examples:
# assert stock_profit([2, 3, 4, 5]) == 3
# assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
# assert stock_profit([4, 3, 2, 1]) == 0
# assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4

# Preconditions:

# len(stock) > 1;
# 0 <= price <= 1000.

# ___________________________________________________________________________________
# Вы являетесь брокером на фондовой бирже. 
# Вы решили совершить всего одну завершенную операцию: купить акцию и продать ее позже, 
# чтобы получить прибыль. “Короткие продажи” 
# (сначала продайте, позже купите) на этом рынке запрещены.

# Цены покупки и продажи в каждый отдельный момент одинаковы 
# (в каждый момент вы можете либо приобрести акцию по цене x, либо продать акцию 
# (если она у вас есть) по той же цене x) и указаны в данном списке акций.

# Итак, вы должны выбрать, по каким ценам лучше всего купить акцию, 
# а затем продать ее, чтобы получить максимальную прибыль от операции. 
# Ваша функция должна возвращать эту максимально возможную прибыль. 
# Если невозможно получить какую-либо прибыль при заданных ценах (это <= 0), ваша функция должна возвращать 0.

# Входные данные: Цены на акции в виде списка целых чисел.

# Результат: Максимально возможная прибыль в виде целого числа.

# ___________________________________________________________________________________
# SOLUTION 17. <>
def stock_profit(stock: list[int]) -> int:
    buy_price = stock[0]
    idx_list = range(0, len(stock) - 1)
    idx = 0
    for i in idx_list:
        if stock[i] < buy_price:
            buy_price = stock[i]
            idx = i
    
    new_stock = stock[idx:]
    max_price = max(new_stock)
    return max_price - buy_price

print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0


# <><><><><> Best "Clear" Solution <><><><><>
stock_profit = lambda s: max([s[i] - min(s[:i]) for i in range(1, len(s))] + [0])

# <><><><><> Best "Creative" Solution <><><><><>
stock_profit=p=lambda s:len(s)and max(max(s)-s[0],p(s[1:]))

# <><><><><> Best "Speedy" Solution <><><><><>
def stock_profit(stock: list) -> int:
    n=1
    profits=[0]
    for buy in stock:
        
        for sell in stock[n:]:
            profits.append(sell-buy)
        n+=1
    return max(profits)

# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
def stock_profit(stock: list[int]) -> int:
    mins = stock[0]
    prof = []
    for mins in stock:
        maxs = max(stock[stock.index(mins):])
        prof.append(maxs-mins)
    return max(prof)
# ___________________________________________________________________________________
# ___________________________________________________________________________________
