# 4. Bitwise
# &
# |
# ^
# ~
# >>2
#2<<

a = 5
b = 20
5 << 1
b >> 1

# 5. Assignment

a = 2

a = a+ 2
a +=2

# 6. Membership

"A" not in  "India"

# if-else
# if-elif-else
# nested if-else


entry_price = 145.0  # Entry price for the stock
exit_price = 155.0  # Target exit price for the stock
stop_loss_price = 144.0  # Stop loss price
shares_count = 10  # Number of shares considering buying
account_balance = 900.0  # Current trading account balance
total_cost = entry_price * shares_count

if entry_price > exit_price:
    print("Entry price is greater than exit price")
elif entry_price > stop_loss_price:
    print("Enter price is greater than SL price")
    if shares_count > 5:
        print("Share count is greater than 5")
    else:
        print("Share count is not greater than 5")

else:
    print("Both the conditions are not true")

#math.factorial()
#math.floor()
#math.sqrt()
import math
math.factorial(5)
math.ceil(6.1)
math.sqrt(196)

#random.randint(1,100)
import random
random.randint(1,100)

#datetime.datetime.now()
import datetime
print(datetime.datetime.now())
#Initial Stock Price and Volatility

#Initial Stock Price and Volatility
import random
import datetime

initial_price = 150
volatility = 0.05

volatility_change = random.choice([-volatility,volatility])

daily_price_change = initial_price + (initial_price*volatility_change)

today = datetime.datetime.today()

print("Today's Date "  , today)
print("Initial price "  , initial_price)
print("New  price "  , daily_price_change)

# While Loop
#Example - Target Price

current_price = 150
target_price  = 155

while current_price < target_price:
    print("Price is still below the target price")
    current_price += 1

print("Now the Price is above the target price and you can sell the stock")

# While Else with Example

price = [120,112,114,111,112]
threshold_price = 115
index = 0

while index < len(price):
    if price[index] > threshold_price:
        print(f"The price  {price[index]} breaches the threshold price {threshold_price} at {index}  ")
        break
    index += 1
else:
    print("There is no price breach")

print("Search is completed")

# For Loop
# Example - Average Closing Price over a 5-day period
closing_price = [120,112,114,111,112]

total_price = 0

for i in closing_price:
    total_price += i
avg_closing_price = total_price / len(closing_price)
print("The average closing price of 5 days is " , avg_closing_price)
