"""
1. List Operations (append, extend, insert)
Question: You have a list of current holdings in your portfolio. Add new stocks at the end, a list of upcoming
stocks in the middle, and a special stock at the beginning.
"""
from calendar import prcal
from dis import print_instructions
from os import remove
from traceback import print_tb

from pandas.core.arrays.categorical import contains
from pycparser.ply.cpp import t_CPP_ID

data  = ['AAPL','MSFT']
numberOfStock = int(input("enter the number of stocks: "))
'''for i in range(numberOfStock):
    values = input("enter the name of the stock: ")
    data.append(values)'''
for i in range(numberOfStock):
    '''l = []
    values = input("enter the name of the stock: ").upper()
    l.append(values)
    data.insert(1, values)'''

for j in range(numberOfStock):
    values = input("enter the name of the stock: ").upper()
    data.insert(0, values)

print(data)


"""
2. Editing and Deleting Items
Question: From the given list of stock symbols, change the symbol 'GOOG' to 'GOOGL' and remove 'NFLX' from the list."""

lst = ['GOOG', 'MSFT', 'TSLA', 'NFLX']
for i in range(len(lst)):
    if lst[i] == "GOOG":
        lst[i] = "GOOGL"
    if lst[i] == "NFLX":
        lst.remove(lst[i])
print(lst)



"""
3. Zip and Loop Operations
Question: Given two lists, stock_symbols and stock_prices, use the zip() function to pair each stock with its price 
in a dictionary. Then print each pair.
"""

stock_symbols = ['AAPL', 'MSFT', 'ETH', 'BTC']
stock_prices = [1002.21, 1212.34, 1211.5, 9933.34]
zzip = list(zip(stock_symbols, stock_prices))
print(zzip)

dict = dict(zip(stock_symbols, stock_prices))
print(dict)


"""
4.Complex List Manipulation and Conditional Logic
Question: Given a list of stock prices, create a new list that contains the price increased by 5% for only those 
prices that are below $200. Additionally, print the index of each modified price in the original list.
"""
prices = [1000,121,171,900,290,466,321,876,300,487,653]
updated_price = []
for i in prices:
    if i < 200:
        increased = i + i*5/100
        i = increased
        updated_price.append(i)
    else:
        updated_price.append(i)
print(prices)
print(updated_price)


"""
5. Advanced List Comprehension with Conditional Logic
Question: You have a list of stock symbols and their corresponding prices. Use list comprehension to create a list 
of tuples for only those stocks with prices over $100, and sort this list by price in descending order.
"""

stock_symbols = ["AAPL", "GOOG", "MSFT", "TSLA", "NFLX", "META"]
stock_prices = [150, 2800, 95, 720, 85, 310]

zip_list1 = list(zip(stock_symbols, stock_prices))
zip_list = zip_list1

print(zip_list1)
for i in zip_list:
    if i[1] < 100:
        zip_list.remove(i)
    else:
        continue
ordered_list = sorted(zip_list, key=lambda x: x[1], reverse=True)
print(ordered_list)


"""
6. Nested Loops and List Operations
Question: You have a list of lists where each sublist contains stock symbols followed by their daily closing prices 
over a week. Create a flattened list of symbols paired with their average weekly price.
"""
stock_data = [
    ["AAPL", 150, 152, 148, 149, 151],
    ["GOOG", 2800, 2820, 2790, 2810, 2805],
    ["MSFT", 295, 297, 294, 296, 298],
    ["TSLA", 720, 725, 715, 730, 735]
]
ticker = []
print()

for i in stock_data:
    ticker.append(i[0])
    combined_avg = []
    data = []
    for k in i:
        if k == i[0]:
            continue
        else:
            data.append(k)
            avg = sum(data)/len(data)
            combined_avg.append(avg)
print(ticker)
print(combined_avg)

final_ans = list(zip(ticker, combined_avg))
print(final_ans)


"""
7. Complex List Manipulation Using Del and Slicing
Question: Given a list with stock prices, delete prices that are exactly $100, and replace the last three elements 
with their mean.
"""

prices = [120, 100, 95, 100, 110, 105, 100, 115, 98, 102]

for i in prices:
    if i == 100:
        prices.remove(i)
print(prices)

last_3ele = prices[-3:]
print(last_3ele)
mean = sum(last_3ele)/len(last_3ele)
prices[-3:] = [mean]

print(prices)


"""
8. List Comprehension and Functional Programming
Question: Using a list of numbers, create a new list that contains the square of each number, but only if the number 
is odd.
"""

numbers = [1,2,3,4,5,6,7,8,9,10,11]
filtered = (filter(lambda x:x%2 ==1, numbers))
ans = list(map(lambda x:x**2, filtered))
print(ans)


"""
9. Complex List Operations with String Manipulation
Question: Given a list of strings representing transactions, parse each string into a tuple containing the type of 
transaction ('Buy' or 'Sell') and the amount, then filter out any transactions under $200.
"""
transactions = [
    "Buy:150",
    "Sell:250",
    "Buy:300",
    "Sell:100",
    "Buy:500",
    "Sell:180",
    "Buy:220"
]
new = []
action = []
cost = []
print()
for i in transactions:
    lst = i.split(":")
    action.append(lst[0])
    cost.append(lst[1])

net_value = list(zip(action, cost))
print(net_value)

for i in net_value:
    if int(i[1]) < 200:
        net_value.remove(i)
    else:
        continue
print(net_value)


"""
10. List and Error Handling
Question: Attempt to access the 10th element of a list that contains only 5 elements. Use exception handling to manage 
the potential IndexError and print a custom error message.
"""
stocks = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]

stocks = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]

try:
    print("10th stock:", stocks[9])  # Index 9 is the 10th element
except IndexError:
    print("Error: Tried to access the 10th element, but the list has only", len(stocks), "elements.")

