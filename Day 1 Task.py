"""Python Mini Project 1 :
Scenario: Stock Data Entry and Analysis Tool

Objective: Create a Python script that will involve taking manual input for stock prices over a week and will
calculate the average price. It should also demonstrate variable declaration, user input, and basic arithmetic
using Python types."""
from numpy.ma.extras import average

stock_prices = []
dates = int(input("enter the no of days of data required: "))
for i in range(0,dates):
    data = float(input(f"Enter the data of the price of APPLE (AAPL) of the past {dates} days: "))
    stock_prices.append(data)
print(f"The stock prices provided: {stock_prices}")
avg = sum(stock_prices)//len(stock_prices)
print(f"The Average of the prices: {avg}")