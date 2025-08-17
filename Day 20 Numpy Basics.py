from xml.sax.handler import property_interning_dict

import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table

#1-D array:
a = np.array([1,2,3,4,5])
b = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(a)
print(b)

#dtppe:
d1 = np.array([1,2,3,4,5], dtype = np.int32)
d2 = np.array([1,2,3,4,5], dtype = str)          #String DataType
print(type(d1))
print(d2)

#arange
data = np.arange(2,9,2)
print(data)

d2 = np.arange(0,12).reshape(2,6)
d3 = np.arange(0,12).reshape(2,3,2)
d4 = np.arange(0,12).reshape(2,2,3)
print(d2)
print()
print(d3, end=' ')
print()
print(d4)

#---------- Final code -----Exercise--------->
a1 = np.arange(11)
a2 = np.arange(12).reshape((3,4))
a3 = np.arange(27).reshape((3,3,3))

one = np.ones((2,5))
print(one)

zero = np.zeros((3,3))
print(zero)

rand = np.random.random((2,4))
print(rand)

#linspace
lin = np.linspace(-10,10,5)
print(lin)

#Array Attributes...

#ndim
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

#size
print(a1.size)
print(a2.size)
print(a3.size)

#dtype:
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

#changing datatypes...

a1.astype(np.int32)
a2.astype(str)

#Array Operations...

#1. Scalar:
print()
print(a2*2)

#2. Relational
print(a2 ==6)
print(a3<12)

#3. Vector operations...
a4 = np.arange(10,22).reshape(3,4)
print()
print(a2)
print()
print(a4)
print()
print(a2+a4)
print(a2/a4)
print(a2-a4)
print(a2*a4)
print()
#Array Functions...
print(
    a2
)
print(np.max(a2))
print(np.max(a2, axis = 1))     #max of the rows
print(np.max(a2, axis = 0))     #max of columns

#Dot Product

a5 = np.arange(9).reshape((3,3))
print()
print(np.dot(a5,a2))

#Indexing...Slicing
print()
# print(a2)
# print(a2[1,2])
print(a3)
print()
print(a3[1,1,1])
print(a3[2,1:,1:])

p0 = np.arange(27).reshape((3,3,3))
print(p0)
print()

#accesing top corners of the oth and 2nd matrix with p...
print(p0[::2,0,0::2])

ohlc_data_day1 = np.array([
    [100.1, 101.5, 99.5, 101.0],
    [101.3, 102.9, 100.5, 101.8],
    [101.8, 103.0, 101.0, 102.5]
])

ohlc_data_Day2 = np.array([
    [200.0, 201.5, 299.5, 201.0],
    [201.0, 202.0, 200.5, 201.8],
    [201.8, 203.0, 201.0, 202.5],
    [201.8, 203.0, 201.0, 202.5]
])

a6 = [1,2,3,4,5]
for i in np.ravel(ohlc_data_day1):
    print(i)
print()
# Transpose
print(np.transpose(ohlc_data_day1))
print(ohlc_data_day1.T)

# ravel
print(np.ravel(ohlc_data_day1) )

# horizontal stacking

ohlc_data_day1 = np.array([
    [100.1, 101.5, 99.5, 101.0],
    [101.3, 102.9, 100.5, 101.8],
    [101.8, 103.0, 101.0, 102.5]
])

ohlc_data_Day2 = np.array([
    [200.0, 201.5, 299.5, 201.0],
    [201.0, 202.0, 200.5, 201.8],
    [201.8, 203.0, 201.0, 202.5]

])

x= np.hstack((ohlc_data_day1, ohlc_data_Day2))
print(x)


# Vertical stacking
y = np.vstack((ohlc_data_day1,ohlc_data_Day2))
print(y)

# horizontal splitting
print(np.hsplit(x,2), end=" \t")