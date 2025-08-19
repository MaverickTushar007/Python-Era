#Numpy Advanced...
import numpy as np

#Fancy Indexing--->
a =  np.arange(0,12).reshape(4,3)
print(a)
print()
print(a[[0,2,3]])
print()
#for Rows...
a1 =  np.arange(0,12).reshape(3,4)
print(a1[:,[0,2,3]])
print()
#Boolean Indexing...

b = np.random.randint(0,100,24).reshape(6,4)
print(b)
#to find all the numbers >50:
print()
print(b[b>50])

#> 50 and even....
print(b[(b>50) & (b%2 == 0)])

# not divisible by 7:
print(b[~(b%7==0)])


# Broadcasting...

x = np.arange(3).reshape(1,3)
y = np.arange(4).reshape(4,1)

print()
print(x+y)
print()


'''
x1 = np.arange(3).reshape(1,3)
y1 = np.arange(12).reshape(3,4)
print()
print(x1+y1)
'''

#Working with Mathematical functions...

#sigmoid fx = 1/(1+exp(-x))
def sigmoid(array):
    return 1/(1+np.exp(-array))

z = np.arange(10)
print(z)
print()
print(sigmoid((z)))

#mean Square Error...
# [1/n * summation(yi - y0)^2]


def mse(actual, predicted):
    result = np.mean((actual - predicted)**2)
    return result

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)
print()
print(mse(actual, predicted))
print()
#working with the missing values...

a2 = np.array([1,2,3,4,5,np.nan,7,np.nan])
print(a2)

print(a2[~(np.isnan(a2))])


#plotting graphs...
import matplotlib.pyplot as plt

# y = x

p1 = np.linspace(0,100,25)
y = p1
# plt.plot(p1, y)
# plt.show()

# y = x^2

p2 = np.linspace(-100,100,25)
y = p2 ** 2
# plt.plot(p2, y)
# plt.show()


# y = xlog(x)
p3 = np.linspace(-100,100,25)
y = p3 * np.log(p3)
# plt.plot(p3, y)
# plt.show()


# [1/n * summation(yi - y0)^2]
p4 = np.linspace(-100,100,25)
y = 1/(1+np.exp(-p4))
plt.plot(p4, y)
plt.show()