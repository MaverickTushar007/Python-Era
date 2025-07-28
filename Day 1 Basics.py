#Printing Single Data Type
print("Hello World !")
#Printing Multiple Data Types
print("String",100 ,[1,2,3], 1.2,{"key":"value"}, sep="-" )
#Separator

#End
print("Hello World !", end="-")
print("This is Kuldeep",end="-")
print("We are The Unstoppable")

#Integers

print(1)
print(type(1))

#Float
print(1.2)
print(type(1.2))

#Boolean
print(True)
print(type(True))

#Strings
strings = "100 Days of Hell with Python Algotrading"
print(strings)
print(type(strings))

#Complex
complex = 2+3j
print(complex.imag)
print(type(complex))

#List
list = [1,2,"Kuldeep", 1.2]
print(list)
print(type(list))


#Tuples
Tuples = (1,2,"Kuldeep", 1.2)
print(Tuples)
print(type(Tuples))

#Sets
set = {1,2,"Kuldeep", 1.2}
print(set)
print(type(set))

#Dictinary
dict = {"key1":1,"key2":2,"key3":"Kuldeep", "key4":1.2}
print(dict.keys())
print(type(dict))

# How to declare/create a variable ?
a = 1
b = "Apple Stocks"
# Dynamic Typing
a = 1
b = "Kuldeep"
# Dynamic Binding
a = 1
a = "Kuldeep"
a = [1,2,3]
# Stylish techniques for variable declaration
'''int a = 1
int b = 2
int c = 3
'''
a,b,c = 1,2,3

a=b=c=1

# Implicit Vs Explicit
price1 = 100
price2 = "200"
total= price1 +int(price2)
total

# 1. Binary Literals
a = 0b1001
# 2. Decimal Literals
b = 301
# 3. Octal Literals
c = 0o321
# 4. Hexadecial Literals
d = 0x21b

# 5. Float Literals
e = 1.2
# 6. Complex Literals
f  = 1+2j
# 7. String Literals
h =  "it's a string1"
  # ' '
  # " "
  # ''' '''
  # Unicode
unicode_str = u"\U0001F923\U0001f600"
  # Raw
raw_str = r"raw \n string"
print(raw_str)