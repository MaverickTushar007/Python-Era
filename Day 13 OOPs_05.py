#Method Overriding
class TradingStrategy:
    def execute(self):
        print("Executing base strategy")

class EMAStrategy(TradingStrategy):
    def execute(self):
        print("Executing EMA strategy")

# Usage
strategy = EMAStrategy()
strategy.execute()  # Output: Executing EMA strategy
print()


#Method Overloading
class TradingStrategy:
    # Method to execute the strategy with no parameters
    def execute(self, times=1, strategy_name="default"):
        for i in range(times):
            print(f"Executing {strategy_name} trading strategy, run {i + 1}")

### Usage
strategy = TradingStrategy()
strategy.execute(2,"AwesomeStrategy")
print()

#Operator Overloading
class TradingStrategy:
    def __init__(self, profit):
        self.profit = profit

    def __add__(self, other):
        return TradingStrategy(self.profit + other.profit)

    def __str__(self):
        return f"Total Profit: ${self.profit}"

# Usage
strategy1 = TradingStrategy(500)
strategy2 = TradingStrategy(300)
combined_strategy = strategy1 + strategy2
print(combined_strategy)  # Output: Total Profit: $800

#Abstraction

'''
Explanation:
Base Abstract Class (TradingApp):

connect: Concrete method for connecting to the trading server.
strategy: Abstract method to be implemented by subclasses.
execute_trade: Abstract method to be implemented by subclasses.
Derived Class (EMATradingApp):

mobile_login: Additional method specific to the mobile trading app.
strategy: Implements the abstract method with a specific strategy (EMA).
execute_trade: Implements the abstract method to execute a trade based on the EMA strategy.
Usage:
An instance of EMATradingApp is created.
The connect method is called to simulate connecting to a trading server.
The mobile_login method is called to simulate logging into the mobile trading app.
The strategy method is called to specify the EMA trading strategy.
The execute_trade method is called to execute a trade based on the EMA strategy.
'''
print()

from abc import ABC, abstractclassmethod
class  TradingBot(ABC):
    # @abstractclassmethod      # if this used and connect method is not found in the other class then it won't work.
    def connect(self):
        print("connected to the trading server")
    @abstractclassmethod
    def strategy(self):
        pass

    @abstractclassmethod
    def execute_trade(self):
        pass

class EMATradingApp(TradingBot):
    def mobile_login(self):
        print("Logged into the mobile app")

    def strategy(self):
        print("Using the EMA strategy")

    def execute_trade(self):
        print("Executing trade based on EMA")

app = EMATradingApp()
app.connect()           # Output: Connected to trading server
app.mobile_login()      # Output: Logged into mobile trading app
app.strategy()          # Output: Using EMA trading strategy
app.execute_trade()     # Output: Executing trade based on EMA strategy

#absMethod = TradingBot()  # Can't instantiate abstract class TradingBot without an implementation for abstract methods
#print(absMethod.strategy())


"""

With abstract methods → Python enforces a rule
“Every subclass must have these methods, or it won’t work.”

"""