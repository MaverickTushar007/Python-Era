from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

with open('sample.txt','w') as f:
  f.write('hello world')
# try catch demo
try:
  with open('sample1.txt','r') as f:
    print(f.read())
except:
  print('sorry file not found')

  # catching specific exception
  try:
      m = 5
      f = open('sample1.txt', 'r')
      print(f.read())
      print(m)
      print(5 / 2)
      L = [1, 2, 3]
      L[100]
  except FileNotFoundError:
      print('file not found')
  except NameError:
      print('variable not defined')
  except ZeroDivisionError:
      print("can't divide by 0")
  except Exception as e:
      print(e)



# else
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())


# finally
# else
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())
finally:
  print('ye to print hoga hi')


# raise ZeroDivisionError('aise hi try kar raha hu')
print()


class Bank:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise Exception('amount cannot be -ve')
    if self.balance < amount:
      raise Exception('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
  obj.withdraw(15000)
except Exception as e:
  print(e)
else:
  print(obj.balance)
print()
print()


class MyException(Exception):
  def __init__(self,message):
    print(message)

class Bank:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise MyException('amount cannot be -ve')
    if self.balance < amount:
      raise MyException('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
  obj.withdraw(5000)
except MyException as e:
  pass
else:
  print(obj.balance)

print()


class SecurityError(Exception):

  def __init__(self,message):
    print(message)
print()
print()
def logout(self):
    print('logout')

class Google:
    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,email,password,device):
        if device != self.device:
            raise SecurityError('bhai teri to lag gayi')
        if email == self.email and password == self.password:
            print('welcome')
        else:
            print('login error')



obj = Google('nitish','nitish@gmail.com','1234','android')

try:
  obj.login('nitish@gmail.com','1234','windows')
except SecurityError as e:
    e.logout()
else:
  print(obj.name)
finally:
  print('database connection closed')