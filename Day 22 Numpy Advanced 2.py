import numpy as np
from PIL.DdsImagePlugin import item1

a = np.array([1,2,34,4,2,3,6,74,243,333])
b = np.arange(12).reshape(4,3)


#np.sort
print(np.sort(a))
print(np.sort(b, axis = 0))
print()
print(b)

print(np.sort(a)[::-1])         # sort descending for 1D
print(np.sort(b, axis=0)[::-1]) # descending column-wise
print(np.sort(b, axis=1)[:, ::-1]) # descending row-wise


#np.append()
print(np.append(a,200))
print(np.append(b, (np.ones((b.shape[0], 1)))))
print()
#np.concatenate
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d), axis = 0))
print(np.concatenate((c,d), axis = 1))

#np.unique

x = np.array([11,2,3,4,51,2,3,4,54,3,1,1])
print(np.unique(x))

#np.expand_dims
# print(np.expand_dims(x,   axis= 0).shape)
print(x.shape)


#np.where
print(np.where(x>50, 100, x))

#np.argmax / argmin
print(np.argmax(x))
print(np.argmin(x))
print()

#np.cumsum() ?/ np.cumprod()
print(b)
print(np.cumsum(b, axis = 0))
print(np.cumsum(b, axis = 1))
print(np.cumprod(b, axis = 1))

#np.percentile()
print(np.percentile(a,100))
print(np.percentile(a,0))
print(np.percentile(a,50))
print(np.median(a))

#np.histogram
print(np.histogram(a, bins = [0,10,20,30,40,50,60,70,80,90]))

#np.corrcoef()
salary = np.arange(10)
exp  = np.arange(10,20)
print(np.corrcoef(salary, exp))

#np.isin()      #membership operator
item1 = np.array([11,20,30,40,50,60,70,80,90, 243])
print(np.isin(a,item1))
print(a[np.isin(a,item1)])

#np.flip()
print(np.flip(b, axis=1))
print(np.flip(b, axis=0))

#np.put -----> permanent changes
np.put(a, [0,1,2], [100,200,300])
print(a)


#np.delete
print(np.delete(a, [5,6,7]))

#set Functions...
m = np.arange(10)
n = np.arange(5, 15)

print(np.union1d(m,n))
print(np.intersect1d(m,n))
print(np.setdiff1d(n,m))
print(np.setdiff1d(m,n))
print(np.setxor1d(m,n))


#np.clip
print(np.clip(m, a_min = 2, a_max = 7))