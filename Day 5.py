# empty
t1= ()
print(type(t1))
# create a tuple with a single item
t2 = ("Tuples",)
print(type(t2))
# homo
t2 = ("Tuples","BTC","ETH")
print(t2)
# hetero
t2 = (1,"BTC",1.5,True)
print(t2)
# tuple

# using type conversion
type(tuple("BTC"))

t2 = (1,"BTC",1.5,True)
t2[3]

t2[-3:-1]

# immutable just like strings
t2 = (1,"BTC",1.5,True)

# t2[1] = "Eth"

t2 = (1,"BTC",1.5,True)

# not possible

t2 = (1,"BTC",1.5,True)

del t2
# print(t2)

# + and *
t2 = (1,"BTC",1.5,True)
t3 = (2,"ETH",2.5,False)
t2+t3

t2*2
# membership

"BTC" not in t2
# iteration

for i in t2:
    print(i)
for j in t3:
    print(j)

# len/sum/min/max/sorted
t2 = (1,"BTC",1.5,True)
t3 = (1,2,3,4)
sorted(t3,reverse=True)

# count


t2 = (1,"BTC",1.5,True,1,"BTC",1.5,True,1,"BTC",1.5,True)
t2.count("BTC")

# index
t2 = (2,3,1,"BTC",1.5,True,1,"BTC",1.5,True,1,"BTC",1.5,True)
t2.index("BTC")

import time
import sys

# Number of elements to use in lists and tuples
num_elements = 1000000

# Sample data generation
data = list(range(num_elements))

# Measure memory sizes
data_list = data[:]
data_tuple = tuple(data)

list_size = sys.getsizeof(data_list)
tuple_size = sys.getsizeof(data_tuple)

print(f"Size of the list: {list_size} bytes")
print(f"Size of the tuple: {tuple_size} bytes")

# Time measurement for creation
start_time = time.time()
data_list = list(range(num_elements))
end_time = time.time()
print(f"List creation time: {end_time - start_time} seconds")

start_time = time.time()
data_tuple = tuple(range(num_elements))
end_time = time.time()
print(f"Tuple creation time: {end_time - start_time} seconds")


# Time measurement for access
start_time = time.time()
for _ in range(1000000):
    _ = data_list[500000]
end_time = time.time()
print(f"List access time: {end_time - start_time} seconds")

start_time = time.time()
for _ in range(1000000):
    _ = data_tuple[500000]
end_time = time.time()
print(f"Tuple access time: {end_time - start_time} seconds")

# Time measurement for iteration
start_time = time.time()
for item in data_list:
    pass
end_time = time.time()
print(f"List iteration time: {end_time - start_time} seconds")

start_time = time.time()
for item in data_tuple:
    pass
end_time = time.time()
print(f"Tuple iteration time: {end_time - start_time} seconds")

# Time measurement for append (lists only)
start_time = time.time()
for _ in range(10000):
    data_list.append(100)
end_time = time.time()
print(f"List append time: {end_time - start_time} seconds")

# Time measurement for extend (lists only)
start_time = time.time()
data_list.extend(range(10000))
end_time = time.time()
print(f"List extend time: {end_time - start_time} seconds")

start_time = time.time()
data_list.extend(range(10000))
end_time = time.time()
print(f"List extend time: {end_time - start_time} seconds")

# tuple unpacking

date, open_price, high = ("2021-01-01", 100, 110)
#print(date, open_price, high)


date, open_price  = ("2021-01-01", 100)
#print(date, open_price)
# Wrong

# Parsing Historical Trade Data

# Historical trade data
trade_data = [
    ("2021-01-01", 100, 110, 95, 105, 1500),
    ("2021-01-02", 106, 112, 100, 110, 2000),
    ("2021-01-03", 111, 115, 105, 113, 1800),
]

# Extract and print closing price and volume
for date, open_price, high, low, close, volume in trade_data:
    print(f"Date: {date}, Close: {close}, Volume: {volume}")

a,b,*others = (1,2,3,4,6,7,8,9)
# print(a,b)
# print(others)

date, open_price, *others = ("2021-01-02", 106, 112, 100, 110, 2000)
print(date)
print(open_price)
print(*others)

# zipping tuples

trade_log  =  ("2021-01-02", 106)
trade_log1 =  ("2021-01-02", 106)

tuple(zip(trade_log,trade_log1))

# empty
# s1 = set()
# s1
# print(type(s1))
# 1D and 2D

#print((s1))
# s1 = {'AAPL', 'GOOGL', 'TSLA'}
# s1

#2D
# s1 = {'AAPL', 'GOOGL', 'TSLA',('MSFT','META')}
# s1
#mutable items

# homo and hetero
# s1 = {'AAPL', 'GOOGL', 'TSLA',{'MSFT','META'}}
# print(s1)

# s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}
# print(s2)
# # using type conversion

# s3 = set('AAPL')
# print(s3)
# print(type(s3))
# duplicates not allowed

# set can't have mutable items

t2 = {1,"BTC",1.5,True}
# t2[0]

t2 = {1,"BTC",1.5,True}
# t2[1] ='ETH'

t2 = {1,"BTC",1.5,True}

# add
t2.add("ETH")
t2
# update
t2.update(["ETH","BTC","XRP"])
t2

# del
t2 = {1,"BTC",1.5,True}
# t2
# del t2[0]
# t2
# print(s)
#del s[0]
# print(s)
# discard
t2.discard("BTC")
t2
# print(s)
# remove
t2.remove(1.5)
t2
# print(s)
# pop
#s.pop()
# clear
#s.clear()
#print(s)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
s1 = {'AAPL', 'GOOGL', 'TSLA'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}
#s1 | s2
# Union(|)
# Intersection(&)
#s1 & s2
# Difference(-)
#s1 - s2
#s2 - s1
# Symmetric Difference(^)
#s1 ^ s2
# Membership Test
#'AAPEL'  in s1
# Iteration
# for i in s1:
#   print(i)

# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
len(s)
sum(s)
min(s)
max(s)
sorted(s,reverse=True)

s1 = {'AAPL', 'GOOGL', 'TSLA','BTC'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}
# union/update


#s1 | s2
s1.union(s2)
s2.update(s1)
s2

# print(s2)

s1 = {'AAPL', 'GOOGL', 'TSLA','BTC'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}

# intersection/intersection_update


s1.intersection(s2)
s1.intersection_update(s2)
s1

# print(s2)

s1 = {'AAPL', 'GOOGL', 'TSLA','BTC'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}

# difference/difference_update


s2.difference(s1)
s2.difference_update(s1)


print(s2)

s1 = {'AAPL', 'GOOGL', 'TSLA','BTC'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}
# symmetric_difference/symmetric_difference_update
s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)

# isdisjoint/issubset/issuperset
s1 = {'AAPL', 'GOOGL', 'TSLA'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}

s2.issuperset(s1)

# copy
s1 = {'AAPL', 'GOOGL', 'TSLA'}
s2 = {'AAPL', 'GOOGL', 'TSLA','MSFT','META'}

s3 = s1.copy()
print(id(s1))
print(id(s3))

# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

fs1 | fs2

# examples

{i**2 for i in range(1,11) if i>5}

# empty dictionary
d = {}
d
# 1D dictionary
stock_prices = { 'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58,'MSFT': 299.35}
stock_prices
# # with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
d2
# # 2D dictionary -> JSON
stock_data = {
    'AAPL': {
        'price': 145.09,
        'volume': 74232000
    },
    'GOOGL': {
        'price': 2731.23,
        'volume': 1203400
    },
    'TSLA': {
        'price': 673.58,
        'volume': 33012300
    },
    'MSFT': {
        'price': 299.35,
        'volume': 27809000
    }
}

stock_data
# # using sequence and dict function
d4 = dict([('stock','AAPL'),('price',673.58),(3,3)])
d4
# # duplicate keys
d5 = {'name':'Kuldeep','name':'Singh'}
d5
# # mutable items as keys
d6 = {'name':'Kuldeep',tuple([1,2,3]):2}
print(d6)

# []

# get

stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
print(stock_data['GOOGL'])  # Accessing the price of AAPL

stock_data['MSFT'] = 299.35
print(stock_data)  # Adding MSFT with its price

stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
# stock_data.pop('TSLA')
#   # Removing TSLA from the dictionary
# stock_data.popitem()
# print(stock_data)
# stock_data
# del stock_data['GOOGL']
# stock_data.clear()
# stock_data

# pop
#d.pop(3)
#print(d)
# popitem
#d.popitem()
# d.popitem()
# print(d)
# del
#del d['name']
#print(d)
# clear

stock_data['AAPL'] = 150.00
print(stock_data)  # Updating the price of AAPL

stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
#print('GOOGL' in stock_data)  # Checking if GOOGL is in the dictionary

for i in stock_data.keys():
    print(i)

print(stock_data.get('AYAPL', 'Not Found'))  # Getting the price of AAPL, with a default message if not found

# items/keys/values

stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
stock_data.values()

# update
stock_data.update({'AAaPL': 145.09, 'GOaOGL': 2731.23, 'TaSLA': 673.58})
stock_data

# print 1st 10 numbers and their squares
{i:i**2 for i in range(1,11)}

# using existing dict

stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
stock_data = {symbol: price * 1.05 for symbol, price in stock_data.items()}
print(stock_data)  # {'AAPL': 152.3445, 'GOOGL': 2867.7915, 'TSLA': 707.259}

# using zip


symbols = ['AAPL', 'GOOGL', 'TSLA']
prices = [145.09, 2731.23, 673.58]
stock_data = {symbol: price for symbol, price in zip(symbols, prices)}
print(stock_data)  # {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}

# using if condition
stock_data = {'AAPL': 145.09, 'GOOGL': 2731.23, 'TSLA': 673.58}
high_value_stocks = {symbol: price for symbol, price in stock_data.items() if price > 1000}
print(high_value_stocks)  # {'GOOGL': 2731.23}

# Nested Comprehension

symbols = ['AAPL', 'GOOGL']
dates = ['2024-05-20', '2024-05-21']
prices = [[145.09, 150.00], [2731.23, 2750.00]]
#historical_prices = {symbol: {date: prices[i][j] for j, date in enumerate(dates)} for i, symbol in enumerate(symbols)}
#print(historical_prices)  # {'AAPL': {'2024-05-20': 145.09, '2024-05-21': 150.0}, 'GOOGL': {'2024-05-20': 2731.23, '2024-05-21': 2750.0}}
historical_prices = {
    symbol: {
        date: prices[i][j]  # Get the j-th price for the i-th stock (symbol)
        for j, date in enumerate(dates)
    }
    for i, symbol in enumerate(symbols)
}
print(historical_prices)
