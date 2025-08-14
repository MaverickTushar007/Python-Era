# Dostrings...

def docstring():
    """dostring are the simple the texts or the info which make the code more understandable and readable.
        Yeah! it's that easy...
    """
    pass
print(docstring.__doc__)

# Creating a functions...
prices = [1,2,3,4,5,6,7,8,9]
def calculate_sma(prices, window):
    """
    it will calculate simple moving average
    Parameter:
        prices = list of float prices
        window = window size(int)
    """

    if len(prices) < window :
        return ValueError()
    return sum(prices[-window:])/window



print(calculate_sma(prices, 5))
print(calculate_sma.__doc__)

# Using *args & **kwargs
def calc_sum(*args):
    return sum(args)

result = calc_sum(102,242,5,24353,352)
print(result)

#Describe Trade...

def desc_trade(**kwargs):
    for (key,value) in kwargs.items():
        print(f"{key} --> {value}")
    return None
desc_trade(symbol = "AAPL", Trade_Type = "short", result = "profit")

# Variable Scope...

def variable_scope(price1, price2):
    sum_prices = price1+price2
    print(sum_prices)
    inside_func = "Im from the inside function"
    print(inside_func)

# print(variable_scope)
variable_scope(10,20)
outside_func = "Im from the outside function"
print(outside_func)

