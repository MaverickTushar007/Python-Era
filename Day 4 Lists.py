
trade_logs = [100,"BTC",110.9,True]
# print(id(trade_logs))
# print(id(trade_logs[0]))
# print(id(trade_logs[1]))
# print(id(trade_logs[2]))
# print(id(trade_logs[3]))


# print(id(100))
# print(id("BTC"))
# print(id(110.9))
# print(id(True))

# 1D
#Homogeneous
trade_logs = ["100","BTC","110.9","True"]
#Heteregeneous
trade_logs = [100,"BTC",110.9,True]

# 2D
#Homogeneous
#Heteregeneous

trade_logs = [[100,"BTC",110.9,True],200,300]

# Indexing

trade_logs = [[100,"BTC",110.9,True],200,300]
# print(trade_logs[0][1])
# print(trade_logs[-3][-3])

# Positive
# Slicing

trade_logs = [[100,"BTC",110.9,True],200,300]

print(trade_logs[0:2])
print(trade_logs[-3:-1])

# append
trade_logs = [[100,"BTC",110.9,True],200,300]
trade_logs.append([[100,"BTC",110.9,True],200,300])
print(trade_logs)

# extend

trade_logs = [[100,"BTC",110.9,True],200,300]
buy_condition = "Kuldeep"
trade_logs.extend(buy_condition)
print(trade_logs)

# insert
trade_logs = [[100,"BTC",110.9,True],200,300]
trade_logs[0].insert(1,"ETH")
print(trade_logs)

# editing with indexing
trade_logs = [[100,"BTC",110.9,True],200,300]
# trade_logs[1] = 'Eth'
# trade_logs[0][1] = 'XRP'
# trade_logs

# editing with slicing
trade_logs = [[100,"BTC",110.9,True],200,300]
trade_logs[0][:]=[300,"XRP",120,False]
trade_logs

# del
trade_logs = [[100,"BTC",110.9,True],200,300]
# print(trade_logs)
# del trade_logs
# print(trade_logs)



# indexing
trade_logs = [[100,"BTC",110.9,True],200,300]

del trade_logs[1]
print(trade_logs)

# slicing
trade_logs = [[100,"BTC",110.9,True],200,300]
del trade_logs[0][1:3]
print(trade_logs)

# remove
trade_logs = [[100,"BTC",110.9,True],200,300]
trade_logs[0].remove("BTC")
trade_logs

# pop
trade_logs = [[100,"BTC",110.9,True],200,300]
trade_logs[0].pop(-1)
trade_logs

# clear
trade_logs = [[100,"BTC",110.9,True],200,300]
print(trade_logs)
trade_logs.clear()
print(trade_logs)

# Arithmetic (+ ,*)

trade_logs = [[100,"BTC",110.9,True],200,300]
stock_details = [100,120]
new_list = trade_logs + stock_details
# print(new_list)

trade_logs = [[100,"BTC",110.9,True],200,300]
# trade_logs*2
# Concatenation/Merge
# Loops
for i in trade_logs[0]:
    print(i)

# len/min/max/sorted

trade_logs = [[100,"BTC",110.9,True],200,300]
len(trade_logs)

trade_logs = [100,200,300]
min(trade_logs)
max(trade_logs)
sorted(trade_logs, reverse=True)

# count

trade_logs = [100,200,300,100,200,300,100,200,300,100,200,300]
trade_logs.count(100)

# reverse
trade_logs = [100,200,300,100,200,300,100,200,300,100,200,300]
trade_logs.reverse()
trade_logs

# permanently reverses the list

# sort (vs sorted)
trade_logs = [100,200,300,100,200,300,100,200,300,100,200,300]
sorted(trade_logs)
print(trade_logs)
trade_logs.sort()
print(trade_logs)

# copy -> shallow
trade_logs = [100,200,300,100,200,300,100,200,300,100,200,300]
print(trade_logs)
print(id(trade_logs))
new_trade_logs = trade_logs.copy()
print(new_trade_logs)
print(id(new_trade_logs))


# Add 1 to 10 numbers to a list
L = []
for i in range(1,11):
    L.append(i)
print(L)

[i  for i in range(1,11)]

# scalar multiplication on a vector

v = [2,3,4]
s = -3
L = []
for i in v:
    L.append(i*s)
print(L)


[i*s for i in v]

# Add squares

L = [2,3,4,5,6,7,8,9,10]

S = []
for i in L:
    S.append(i**2)
print(S)
[i**2 for i in L]

# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

Z = list(zip(L1,L2))
print(Z)
print([(i+j) for i,j in Z])