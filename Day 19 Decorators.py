'''
Decorators in Python Algorithmic Trading:


Logging:

Automatically log function calls and their results.
Useful for monitoring and debugging trading operations.
Timing:

Measure the execution time of functions.
Important for ensuring the performance of trading algorithms.
Retry Mechanism:

Automatically retry a function if it raises specific exceptions.
Useful for handling intermittent network requests or database operations.
Access Control:

Enforce access controls based on user roles or permissions.
Ensures that only authorized users can perform certain actions.
Resource Management:

Ensure proper acquisition and release of resources like database connections or files.
Helps manage resources efficiently and avoid leaks.
These decorators help improve code maintainability, readability, and functionality in algorithmic trading systems.\
'''
from datetime import datetime
import time

from numpy.ma.core import inner
from pandas.core.construction import sanitize_array


# Python are 1st class function
def modify(func,num):
  return func(num)

def square(num):
  return num**2

modify(square,2)


# simple example
def my_decorator(func):
  def wrapper():
    print('***********************')
    func()
    print('***********************')
  return wrapper

def hello():
  print('hello')

def display():
  print('hello nitish')

a = my_decorator(hello)
a()

b = my_decorator(display)
b()


# Better syntax?
# simple example
def my_decorator(func):
    def wrapper():
        print('***********************')
        func()
        print('***********************')

    return wrapper

@my_decorator
def hello():
    print('hello')

hello()
print()

def modified_Strategy(func):
    def wrapper(dyn_data):
        print(f"*****-----------Initialising Trade :- {datetime.now()} -------------******")
        print(func(dyn_data))
        print(f"*****----------Trade Executed :- {datetime.now()}--------------******")
    return wrapper

@modified_Strategy
def SMAStrategy(price_data):
    prices = price_data['price']
    time.sleep(2)
    sma = sum(prices)/len(prices)
    return sma

trade_data = {'price':[10,20,30,40,50,60]}
# a = modified_Strategy(SMAStrategy)
# a((trade_data))

print(SMAStrategy(trade_data))


#example 2:

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if isinstance(*args,data_type):
                print(func(*args))
            else:
                raise ValueError("Incorrect Datatype")
        return inner_wrapper
    return outer_wrapper


@sanity_check(int)
def square(num):
    return num*num

@sanity_check(str)
def greet(name):
    return f"Hello, {name}"

square(12)
greet("Tushar")
print()

#eg 3:
# anything meaningful?
def timer(func):
  def wrapper(*args):
    start = time.time()
    func(*args)
    print('time taken by',func.__name__,time.time()-start,'secs')
  return wrapper

@timer
def hello():
  print('hello world')
  time.sleep(2)

@timer
def square(num):
  time.sleep(1)
  print(num**2)

@timer
def power(a,b):
  print(a**b)

hello()
square(2)
power(2,3)