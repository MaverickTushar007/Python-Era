#Magic Methods
from soupsieve.css_parser import NEWLINE


class Trades:
    def __init__(self, symbol, price, amount, status):
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.status = status

    def __repr__(self):
        return f'{self.symbol} {self.status} @ {self.price} for {self.amount}'
    def __str__(self):
        return f'{self.symbol} {self.status} @ {self.price} '
    def __add__(self, other):
        if self.symbol == other.symbol:
            new_quantity = self.amount + other.amount
            new_avg = (self.amount*self.price + self.amount*self.price)/new_quantity
            print(f"The total amount of the stock is {new_quantity} with the average amount of ${new_avg}.")
        else:
            print("Both the symbols got to be the same.")

strategy1 = Trades("Eth", 1000, 12, "Bought")
strategy2 = Trades("Eth", 400, 2, "Sold")
print(repr(strategy1))
print(strategy1)             #even if str is not mentioned still it prints the string magic method.

(strategy1+strategy2)


class Trader:
    def __init__(self, name, Trading_style):
        self.name = name
        self.Trading_style = Trading_style

    def greet(self):
        if self.Trading_style == "Day Trading":
            print(f"Good Day for Trading, {self.name}")
        elif self.Trading_style == "Swing Trading":
            print(f"Hope you catch the Swings, {self.name}")
        else:
            print(f"Happy trading, {self.name}")

king = Trader("tushar", " Trading")
king.greet()