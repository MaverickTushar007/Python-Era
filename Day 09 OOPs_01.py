#Human blueprint
'''
from peewee import qualify_names


class Human:
    hands = 2
    legs = 2
    eyes = 2

    def vision(self):
        print("I can see things")
        pass
    def walk(self):
        pass
    def think(self):
        pass

Tushar = Human()
Tushar.vision()
'''

class TradingStrategy:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        self.position = 0

    def Buy(self, price, quantity):
        if self.amount >= price * quantity:
            self.position += quantity
            self.amount -= price * quantity
            print(f"Successfully bought {quantity} shares of {self.symbol} at {price}")
        else:
            print("Not enough funds for the trade.")

    def Sell(self, price, quantity):
        if self.position >= quantity:
            self.position -= quantity
            self.amount += price * quantity
            print(f"Successfully sold {quantity} shares of {self.symbol} at {price}")
        else:
            print("Currently no shares to sell.")

    def status(self):
        print(f"Current position: {self.position} of {self.symbol}")
        print(f"Remaining amount: {self.amount}")


# Example usage
momentum = TradingStrategy("ETH", 5000)
print(momentum.symbol)

momentum.Buy(2000, 2)  # Buy 2 ETH at 2000 each
momentum.status()

momentum.Sell(2200, 1)  # Sell 1 ETH at 2200
momentum.status()
