# Nested Functions...
from traceback import print_list


def Trade_desc(price):
    def buy():
        return "BUY"
    def sell():
        return "SELL"

    if price> 50:
        return buy()
    else:
        return sell()

decision = Trade_desc(400)
print(decision)

#python as also referred to as first class citizens.
# Type and ID...
def Trade(price):
    pass

print(type(Trade(2)))
print(id(Trade(2)))

# deleting a function...
def trading_logs():
    return "this is the way we can delete a function"


print(trading_logs())
'''del trading_logs()'''  #Notes we cant delete a function when its called, consider writing only the name of the function
del trading_logs
# print(trading_logs())

#storing...
def buy_stock(symbol):
    return f"buy {symbol}"
def sell_stock(symbol):
    return f"sell_stock {symbol}"

repo = {"buy": buy_stock, "sell": sell_stock}
print(repo["buy"]("AAPL"))

#returning a function...
def strategy_selection(strategy):
    def momentum_strategy():
        return "Momentum Strategy"

    def mean_reversion_strategy():
        return "mean reversion strategy"

    if strategy != "momentum":
        return mean_reversion_strategy()
    else:
        return momentum_strategy()

strategy = strategy_selection("momentum")
print(strategy)

# function as an argument...
def moving_average_strategy(prices):
    return sum(prices)/len(prices)
def execute_strategy(strategy_func, prices):
    return strategy_func(prices)
prices = [10,30,20,40,45]

solution = (execute_strategy(moving_average_strategy, prices))
print(solution)

# Lambda Function...

# MAP
# squaring of numbers
l1 = [11,12,13,14,15]
sq =  list(map(lambda x:x**2,l1))
print(sq)

# classifying High or Low...
classification = list(map(lambda x:"High" if x>13 else "Low",l1))
print(classification)

# fetching names from the stock data info dictionary...
stocks = [{"symbol": "AAPL", "Name": "Apple"}, {"symbol": "BTC", "Name": "Bitcoin"}]
print(list(map(lambda x: x["Name"],stocks)))

# Filter...
# filtering prices
data = 100,200,200,453,523,432,432,424,243
print(list(filter(lambda x:x>200,data)))

# filter stocks...
stock = ['Apple','Microsoft','Tesla', 'Amazon']
print(list(filter(lambda x:x.startswith("A"),stock)))

# Reduce...
from functools import reduce

# sum...
num = [ 2, 3, 4, 5, 6, 7, 8, 9, 10,1]
result = reduce(lambda x, y: x + y, num)
print(result)

# calculating the minimum...
min = reduce(lambda x,y: x if x<y else y,num)
print(min)

prince = {
    'name': 'Tushar'
}
for stock, price in prince.items():
    print(stock, price)