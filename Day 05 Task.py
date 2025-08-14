"""
1. Market Data Handling with Tuples and Dictionaries
Question: You receive real-time market data in the form of tuples (symbol, price, volume). Store these tuples in a
dictionary where the key is the symbol and the value is a list of tuples containing price and volume. Update the
dictionary with new data and maintain only the last three entries per stock.
"""
from six import wraps

# Sample real-time market data
market_data = [
    ('AAPL', 150.12, 5000),
    ('GOOGL', 2750.45, 3000),
    ('AAPL', 151.00, 4500),
    ('GOOGL', 2748.00, 3200),
    ('AAPL', 152.10, 4700),
    ('GOOGL', 2752.00, 3100),
    ('AAPL', 153.30, 4600),
    ('GOOGL', 2753.10, 3300)
]
tup = []


for i in market_data:
    for j in i:
        tup.append(j)

print(tup)
pass


"""
2. Set Operations for Unique Symbol Tracking
Question: Given a list of transactions where each transaction is a tuple (symbol, type, amount), use a set to 
track unique symbols involved in "sell" transactions.
"""

transactions = [
    ('AAPL', 'buy', 500),
    ('GOOGL', 'sell', 700),
    ('MSFT', 'buy', 300),
    ('TSLA', 'sell', 1200),
    ('AAPL', 'sell', 400),
    ('TSLA', 'sell', 800),
    ('GOOGL', 'buy', 1000),
    ('NFLX', 'sell', 650)
]

result = {symbol for symbol,action,price in transactions if action == "sell"}
print(result)


"""
3. Using Zip() with Tuples for Price Comparison
Question: You have two lists of stock prices at different times. Use zip() to create tuples paired by their indices 
and print those stocks where the price has increased.
"""
prices_time1 = [120, 130, 125, 110, 140]  # Earlier prices
prices_time2 = [125, 128, 130, 115, 138]  # Later prices
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']

for symbol, p1, p2 in zip(symbols,prices_time1, prices_time2):
    if p2>p1:
        print(f"{symbol} has their prices increased from {p1} ---> {p2}")


"""
4. Nested Dictionary Comprehension for Market Analysis
Question: Create a nested dictionary from a list of tuples (symbol, price), categorizing by the first letter of the 
symbol and storing prices in a list.
"""

market_data = [
    ('AAPL', 150),
    ('AMZN', 3300),
    ('GOOGL', 2800),
    ('MSFT', 290),
    ('META', 340),
    ('GOOG', 2750),
    ('ADBE', 500),
    ('MSTR', 620)
]
print()
keys = {}
for key, value  in market_data:
    first_letter = key[0]
    if first_letter not in keys:
        keys[first_letter] = []
    keys[first_letter].append(value)
print(keys)


"""
5. Advanced Set and Tuple Manipulation
Question: Given historical data as a list of tuples (symbol, price), filter out any duplicate entries using set 
operations and return a sorted list of tuples based on the price in descending order.
"""
historical_data = [
    ('AAPL', 150),
    ('GOOG', 2800),
    ('MSFT', 299),
    ('AAPL', 150),     # duplicate
    ('TSLA', 720),
    ('GOOG', 2800),    # duplicate
    ('NFLX', 610),
    ('MSFT', 305)
]
data = {}
for (sym, cost) in historical_data:
        if sym not in data:
            data[sym] = (cost)
print(data)
lst = list(data.items())
print(lst)
sort = sorted(lst,  key = lambda x:x[1], reverse=True )
print(sort)

"""
6. Complex Data Structure for Asset Management
Question: Construct a data structure using dictionaries that maps stock symbols to another dictionary containing lists 
of tuples for different transaction types ('buy' or 'sell').
"""
transactions = [
    ('AAPL', 'buy', 150, '2025-01-10'),
    ('GOOG', 'sell', 2800, '2025-01-12'),
    ('AAPL', 'sell', 155, '2025-01-15'),
    ('MSFT', 'buy', 300, '2025-01-11'),
    ('GOOG', 'buy', 2750, '2025-01-08'),
    ('MSFT', 'sell', 310, '2025-01-20'),
    ('AAPL', 'buy', 145, '2025-01-05')
]

assets = {}

for symbol, action, price, date in transactions:
    if symbol not in assets:
        assets[symbol] = {'buy': [], 'sell': []}
    assets[symbol][action].append((price, date))
print()
print(assets)
for symbol in assets:
    print(f"{symbol}:")
    for action in ['buy', 'sell']:
        print(f"  {action}: {assets[symbol][action]}")


"""
7. Financial Data Analysis Using Zip and List Comprehension
Question: You have separate lists of stock symbols and their respective quarterly returns. Pair them and find those 
with positive returns.
"""

symbols = ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']
returns = [5.2, -3.1, 2.0, -1.5, 4.8]
wrap = list(zip(symbols, returns))
positive_return = filter(lambda x:x[1]> 0,wrap)
print(list(positive_return))


"""
8. Immutable Set for Tracking Unique Transactions
Question: Given a stream of transaction IDs, store these IDs in a frozen set for ensuring that you can safely use 
them as keys or in a set without modification. ----> easy
"""
transaction_ids = ['TX1001', 'TX1002', 'TX1003', 'TX1001', 'TX1004', 'TX1002']

"""
9. Tuple Unpacking in Financial Calculations
Question: You receive data in the form of a list of tuples where each tuple contains a stock symbol, its opening 
price, and its closing price. Calculate the daily change for each stock using tuple unpacking. ----> easy
"""
stock_data = [
    ('AAPL', 170, 175),
    ('GOOG', 2800, 2790),
    ('MSFT', 300, 310),
    ('TSLA', 700, 710)
]


"""
10. Comprehensive Market Snapshot Using Nested Comprehensions
Question: Given a dictionary mapping stock symbols to their daily prices over a week, create a nested dictionary that 
maps each symbol to another dictionary of 'highest' and 'lowest' prices of the week.
"""
weekly_prices = {
    'AAPL': [170, 172, 169, 175, 174, 171, 173],
    'GOOG': [2800, 2820, 2790, 2810, 2830, 2805, 2795],
    'MSFT': [300, 305, 298, 310, 307, 306, 302],
    'TSLA': [700, 710, 705, 720, 715, 705, 710]
}


for key, value in weekly_prices.items():
    d = {
        key :{
            "highest" : max(value),
            "lowest" : min(value)
        }
    }
    print(d)

