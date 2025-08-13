class AutoTrading_Bot:
    def __init__(self, threshold):
        self.threshold = threshold
        self.position = None
        self.priceData = []

    def fetch_market_data(self):
        self.priceData = [69340, 69450, 69666, 69707, 69888]
        print("Market data has been fetched")
        return self.priceData

    def latest_Price(self):
        if self.priceData:
            return self.priceData[-1]
        else:
            None

    def evaluate_price(self):
        if self.threshold < self.latest_Price():
            return "Sell"
        elif self.threshold > self.latest_Price():
            return "Buy"
        else:
            return "Hold"

    def execute_trade(self, action):
        if action =="Sell" and self.position != "Short":
            self.position == "Short"
            return f"the sell trade has been executed and the position is short"
        elif action =="Buy" and self.position != "Long":
            self.position == "Long"
            return f"the buy trade has been executed and the position is long"
        else:
            action == "Hold"
            return f"the trade has to be on Hold these is no significant movement in the price."

    def run(self):
        pass



bot1 = AutoTrading_Bot(69666)
print(bot1.fetch_market_data())
print(bot1.latest_Price())
Action = (bot1.evaluate_price())
print(bot1.execute_trade(Action))
"""
69340, 69450, 69666, 69707, 69888"""