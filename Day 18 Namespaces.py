# local and global
# global var
a = 2

def temp():
  # local var
  b = 3
  print(b)

temp()
print(a)


# local and global -> same name
a = 2
def temp():
    # local var
    a = 3
    print(a)


temp()
print(a)


# local and global -> local does not have but global has
a = 2

def temp():
  # local var
  print(a)

temp()
print(a)

'''
# local and global -> editing global
a = 2
def temp():         
  # local var
  a += 1                #This is something we should not do!!!
  print(a)  

temp()
print(a)
'''


a = 2

def temp():
  # local var
  global a          #only defining global 'a' we can do it!!
  a += 1
  print(a)

temp()
print(a)

'''
# local and global -> function parameter is local
def temp(z):
  # local var
  print(z)

a = 5
temp(5)
print(a)
print(z)'''

print()
# Enclosing scope
def outer(x):
  def inner(x):
    print(x)
  inner(x)
  print('outer function')

outer(12)
print('main program')


print()
#   nonlocal keyword
def outer():
  a = 1
  def inner():
    nonlocal a
    a += 1
    print('inner',a)
  inner()
  print('outer',a)


outer()
print('main program')