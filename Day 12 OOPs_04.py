'''
class AutoTrading_Bot:
    def __init__(self, threshold):
        self.__threshold = threshold
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
        if self.__threshold < self.latest_Price():
            return "Sell"
        elif self.__threshold > self.latest_Price():
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
print(bot1.threshold)               #Data has been put to private.

print(bot1._AutoTrading_Bot__threshold)     #Another way we can access the data ecrypted Data.
'''


# Getters and Setters Methods....
class AutoTrading_Bot:
    def __init__(self, threshold):
        self.__threshold = threshold
        self.position = None
        self.priceData = []

    def getattr(self):
        return self._AutoTrading_Bot__threshold

    def setattr(self, new_threshold):
        if type(new_threshold) == int:
            self._AutoTrading_Bot__threshold = new_threshold
            return self._AutoTrading_Bot__threshold
        else:
            return "Dont try to be oversmart!!"

# bot2 = AutoTrading_Bot(90000)
# print(bot2.getattr())
# print(bot2.setattr("50000"))
# print(bot2.getattr())


class AutoTradingBot:
    def __init__(self, stock_name, threshold):
        self.threshold = threshold
        self.stock_name = stock_name

Bot1 = AutoTradingBot("AAPL", 5000)
Bot2 = AutoTradingBot("BTC", 5700)
Bot3 = AutoTradingBot("MSFT", 2000)
Bot4 = AutoTradingBot("ETH", 5890)
Bot5 = AutoTradingBot("SOL", 1000)

l = [Bot1, Bot2,Bot3, Bot4, Bot5]
for i in l:
    print(i.stock_name, i.threshold)

D = {"p1": Bot1, "p2":  Bot2, "p3": Bot3, "p4":Bot4, "p5": Bot5}
for i in D:
    print(D[i].threshold)


#Static Variable as the counter....
class Trader:
    counter = 0
    def __init__(self, stock_name, threshold):
        self.threshold = threshold
        self.stock_name = stock_name
        Trader.counter += 1                 #accessing the static variable from the Class...
        print(Trader.counter)

Bot1 = Trader("AAPL", 5000)
Bot2 = Trader("BTC", 5700)
Bot3 = Trader("MSFT", 2000)

print()
l = [Bot1, Bot2,Bot3]
for i in l:
    print(i.stock_name, i.threshold )


#Aggregation...Has a relation
class MyTradingBot:
    def __init__(self,name,strategy):
        self.name = name
        self.strategy = strategy
    def Execute(self,price):
        action = self.strategy.Evaluate(price)
        return f"{self.name} is Executing a {action} action."


class AwesomeStrategy:
    def __init__(self,threshold):
        self.threshold = threshold

    def Evaluate(self,latest_price):
        if latest_price > self.threshold:
            return "BUY"
        else:
            return "SELL"

strategy = AwesomeStrategy(100)
mybot = MyTradingBot("AwesomeStrategy",strategy)
print(mybot.Execute(950))
print()
print()
#Inhertance...
class MyBaseStrategy:
    def __init__(self, name, stype):
        self.name = name
        self.stype = stype

    def execute(self):
        print("the execution method of the base strategy has been executed.")

class MyEMAStrategy(MyBaseStrategy):
    def __init__(self, name, stype, lwindow, swindow):
        super().__init__(name, stype)
        self.lwindow = lwindow
        self.swindow = swindow
        print("The constructor function of the EMA strategy has been initialized.")

    def evaluate(self):
        print("the evaluate method of the EMA Strategy has been executed.")

obj1 = MyEMAStrategy("NewStrategy", "Technical", 10, 20)
print(obj1.name)
(obj1.execute())


#Constructor example
class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    def execute(self):
        print("Executing trading strategy")

class MovingAverageStrategy(TradingStrategy):
    pass

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(100000, "Medium", "Moving Average")
ma_strategy.execute()
print()
print()


# constructor example 2

class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    # Getter
    def show_capital(self):
        print(self.__capital)

class MovingAverageStrategy(TradingStrategy):
    def check_capital(self):
        # Attempt to access the private attribute will fail
        print(self.__capital)

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(180000, "Medium", "Moving Average")
ma_strategy.show_capital()  # This will work


print()
print()



class TradingStrategy:
    def __init__(self, capital):
        self.__capital = capital

    def get_capital(self):
        return self.__capital    #within the class we can define a function which can give us the hidden value as well

class MovingAverageStrategy(TradingStrategy):
    def show(self):
        print("This is in MovingAverageStrategy class")

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(9000)

# Accessing the private attribute via the parent's method
print(ma_strategy.get_capital())  # Output: 100000

# Calling the method defined in the child class
ma_strategy.show()  # Output: This is in MovingAverageStrategy class


print()
print()


class TradingStrategy:
    def __init__(self, capital):
        self.__capital = capital

    def get_capital(self):
        return self.__capital

class MovingAverageStrategy(TradingStrategy):
    def __init__(self, short_window, capital):
        # Call the parent class's constructor
        super().__init__(capital)
        self.__short_window = short_window

    def get_short_window(self):
        return self.__short_window

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(20, 100000)

# Accessing the private attribute of the parent class via the parent's method
print("Parent: Capital:", ma_strategy.get_capital())  # Output: Parent: Capital: 100000

# Accessing the private attribute of the child class via the child's method
print("Child: Short Window:", ma_strategy.get_short_window())  # Output: Child: Short Window: 20

print()
print()

class TradingStrategy:
    def __init__(self):
        self.capital = 100000

    def display_capital(self, capital):
        print("TradingStrategy Capital:", self.capital)

class MovingAverageStrategy(TradingStrategy):
    def display_strategy(self, strategy_name):
        print("MovingAverageStrategy:", self.capital)


# Example Method Overriding
class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    def execute(self):
        print("Executing a trading strategy")

class MovingAverageStrategy(TradingStrategy):
    def execute(self):
        print("Executing a moving average strategy")

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(100000, "Medium", "Moving Average")

# Calling the overridden method
ma_strategy.execute()  # Output: Executing a moving average strategy

# Creating an instance of MovingAverageStrategy
strategy = MovingAverageStrategy(5000,"Hard", "Bollinger Bands")


print()
# Super Keyword
class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    def execute(self):
        print("Executing a trading strategy")

class MovingAverageStrategy(TradingStrategy):
    def execute(self):
        print("Executing a moving average strategy")
        # Call the parent class's execute method
        super().execute()

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(100000, "Medium", "Moving Average")

# Calling the overridden method, which in turn calls the parent method
ma_strategy.execute()
print()


# using super outside the class
# Demonstrating super and accessing parent data correctly
class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    def execute(self):
        print("Executing a trading strategy")

    def get_risk_level(self):
        return self.risk_level

class MovingAverageStrategy(TradingStrategy):
    def __init__(self, capital, risk_level, strategy_name, short_window):
        super().__init__(capital, risk_level, strategy_name)
        self.short_window = short_window

    def execute(self):
        print("Executing a moving average strategy")
        super().execute()  # Calling the parent class's method
        print(f"Parent's risk level: {super().get_risk_level()}")

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(100000, "Medium", "Moving Average", 10)

# Calling the overridden method
ma_strategy.execute()
print()

# can super access parent's data?
# using super outside the class

# super -> constructor
class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

class MovingAverageStrategy(TradingStrategy):
    def __init__(self, capital, risk_level, strategy_name, short_window, long_window):
        print('Inside MovingAverageStrategy constructor')
        super().__init__(capital, risk_level, strategy_name)
        self.short_window = short_window
        self.long_window = long_window
        print("Inside MovingAverageStrategy constructor")

# Creating an instance of MovingAverageStrategy
ma_strategy = MovingAverageStrategy(100000, "Medium", "Moving Average", 10, 50)

# Accessing attributes from both the parent and child classes
print(ma_strategy.short_window)  # Output: 10
print(ma_strategy.strategy_name)  # Output: Moving Average


class TradingStrategy:
    def __init__(self, capital):
        self.__capital = capital

    def get_capital(self):
        return self.__capital

class MovingAverageStrategy(TradingStrategy):
    def __init__(self, capital, short_window):
        super().__init__(capital)
        self.__short_window = short_window

    def get_short_window(self):
        return self.__short_window

ma_strategy = MovingAverageStrategy(100000, 20)
print(ma_strategy.get_capital())
print(ma_strategy.get_short_window())
print()

# Single Inheritance
class TradingStrategy:
    def __init__(self):
        self.capital = 100000

class MovingAverageStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.short_window = 20

    def show(self):
        print(self.capital)
        print(self.short_window)

ma_strategy = MovingAverageStrategy()
ma_strategy.show()
print()

# Multilevel Inheritance
class TradingStrategy:
    def __init__(self):
        self.capital = 100000

class MovingAverageStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.short_window = 20

class AdvancedMovingAverageStrategy(MovingAverageStrategy):
    def __init__(self):
        super().__init__()
        self.long_window = 50

    def show(self):
        print(self.capital)
        print(self.short_window)
        print(self.long_window)

ama_strategy = AdvancedMovingAverageStrategy()
ama_strategy.show()
print()

# Hierarchical Inheritance
class TradingStrategy:
    def __init__(self):
        self.capital = 100000

class MovingAverageStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.short_window = 20

class MomentumStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.momentum_window = 10

ma_strategy = MovingAverageStrategy()
mo_strategy = MomentumStrategy()
print(ma_strategy.capital)
print(mo_strategy.capital)
print()

# Multiple Inheritance (Diamond Problem)
class TradingStrategy:
    def __init__(self):
        self.capital = 100000

class TechnicalStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.indicator = "RSI"

class FundamentalStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.metric = "PE Ratio"

class HybridStrategy(TechnicalStrategy, FundamentalStrategy):
    def __init__(self):
        super().__init__()

    def show(self):
        print(self.capital)
        print(self.indicator)
        print(self.metric)

hybrid_strategy = HybridStrategy()
hybrid_strategy.show()
print()

# Hybrid Inheritance
class TradingStrategy:
    def __init__(self):
        self.capital = 100000

class TechnicalStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.indicator = "RSI"

class FundamentalStrategy:
    def __init__(self):
        self.metric = "PE Ratio"

class HybridStrategy(TechnicalStrategy, FundamentalStrategy):
    def __init__(self):
        TechnicalStrategy.__init__(self)
        FundamentalStrategy.__init__(self)          #we didnt use super() here!!

    def show(self):
        print(self.capital)
        print(self.indicator)
        print(self.metric)

hybrid_strategy = HybridStrategy()
hybrid_strategy.show()