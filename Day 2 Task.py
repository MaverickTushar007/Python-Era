"""
1. Operators and Logical Expressions
Question: You have a list of stock prices over 30 days. Write a logical expression that will identify consecutive price
drops over three days or more. For instance, [120, 118, 115, 110] would qualify, but [120, 118, 120, 110] would not.
"""
from pandas.io.formats.format import return_docstring

prices = [118, 115,120, 111, 108 ,101]
for i in range(len(prices)-2):
    if (prices[i] > prices[i+1]) and (prices[i+1] > prices[i+2]):
            print(f"The prices have recently drops over the 3 days")
            break

    else:
        print("No prices have significantly dropped!")
        break
print("successfully Compiled")

"""
2. If-Else Statements
Question: You are designing an algorithm to trade stocks. If the current price of a stock is above the 30-day moving 
average, print "Buy Signal"; otherwise, print "Sell Signal". Assume you have a list of daily prices and that the moving 
average can be calculated.
"""

data = [100,211,234,122,321,333,452,121,111,132]
avg = sum(data)/len(data)
current_price = float(input("Enter the current stock price: "))
if current_price > avg:
    print("BUY")
else:
    print("SELL")
print(f"the Moving Average of the Price: {avg}")



"""
3. Modules (pandas)
Question: Use the pandas library to load a CSV file containing historical trading data and calculate the daily 
percentage change of closing prices over a period of time.
"""



"""
4. While Loop
Question: Create a loop that repeatedly checks a stock price from a real-time source every 3 seconds until the stock 
falls below a threshold value. In this scenario, print "Threshold Exceeded" when the threshold is crossed.
"""

import random
import time
#since I don't have values I'm considering threshold to be as 1000 and consider the price range between 500 and 1200.

threshold = 1000
stock  = [random.randint(500,2000) for x in range(10)]
print(stock)
while True:
    for i in range(len(stock)):
        if threshold > stock[i]:
            print(f"{stock[i]} Threshold Exceed!!")
        else:
            print(f"{stock[i]} Didn't exceeded Threshold!")
        #time.sleep(3)
    break


"""
5. For Loop
Question: You have data on the opening and closing prices of multiple stocks in a portfolio. Using a for loop, 
calculate and print the total daily gain or loss for each stock in the portfolio.
"""
# (opening, closing)
info = [(123,122),(111,100),(132,421),(321,234)]
for i in range(len(info)):
    if info[i][0]> info[i][1]:
        net = info[i][0] - info[i][1]
        print(f"Loss of {net}")
    else:
        net_profit = info[i][1] - info[i][0]
        print(f"Profit of {net_profit}")



"""
6. Nested Loops
Question: Create a nested loop that simulates a simple market-making strategy by placing buy and sell orders over a 
range of prices and volumes. Assume bid prices range from 90 to 100 and ask prices range from 101 to 110.
"""
bid_prices = range(90, 101)      # 90 to 100
ask_prices = range(101, 111)     # 101 to 110
volumes = [10, 20, 50]           # Possible order sizes

for bid in bid_prices:
    for ask in ask_prices:
        for volume in volumes:
            print(f"Placing Buy @ {bid} for {volume} units | Sell @ {ask} for {volume} units")

"""
7. Complex If-Else Logic
Question: You have a complex trading rule where a "Strong Buy" signal is given if the stock price is above both the 
30-day and 50-day moving averages, a "Buy" signal is given if only above the 30-day, a "Hold" signal if above the 
50-day, and a "Sell" signal otherwise. Calculate the signals assuming you have daily prices for at least 50 days.
"""
#  i ll be considering the data for 3 and 5 days...
data_3Days = [300,123,567]
data_5Days =  [300,123,567,236,853]
avg3Days = sum(data_3Days)/len(data_3Days)
avg5Days = sum(data_5Days)/len(data_5Days)

print(
    f"current moving average for 3Days: {avg3Days} & 5 days: {avg5Days}"
)

stock_price = float(input("Enter th current price of the stock: "))
if stock_price > avg3Days and stock_price > avg5Days:
    print("Strong BUY")
elif stock_price > avg3Days:
    print("BUY")
else:
    print("HOLD")



"""
8. Modules (numpy)
Question: Use the numpy module to calculate the rolling average for a window of 5 days over a numpy array containing 
20 stock prices.
"""



"""
9. Optimization with Loops
Question: Calculate the best day to buy and the best day to sell to maximize profit within a list of daily prices 
using a single pass of nested loops.
"""
max_profit = 0
l1 = []
buy = sell = 0
daily_price = [123,303,321,683,487,212,100,65,111,90,123,433]
for i in range(len(daily_price)):
    for j in range(i + 1, len(daily_price)):
        profit = daily_price[j] - daily_price[i]  # Sell - Buy
        if profit > max_profit:
            max_profit = profit
            buy = i
            sell = j
print("Buy on day", buy, "at price", daily_price[buy])
print("Sell on day", sell, "at price", daily_price[sell])
print("Maximum Profit:", max_profit)


"""
10. Scenario Analysis
Question: Given that a certain algorithm follows a strategy where every time a stock gains 5% in value from the 
last recorded price, the program places a sell order. Track the hypothetical prices over 15 days and identify when 
sell orders should be triggered.
"""
dailyPrice = [23,303,3201,683,487,2712,100,650,123,433]
initial = 5
for i in range(len(dailyPrice)-1):
    percentIncrease = (dailyPrice[i+1] - dailyPrice[i])/dailyPrice[i]
    if percentIncrease > initial:
        print(f"SELL: {dailyPrice[i]} percentage increased by{percentIncrease}")
