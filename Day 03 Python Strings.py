from websockets.cli import print_over_input

strategy_name =  "Momentum strategy"
strategy_name_latest = strategy_name + " latest"
strategy_name_latest
del strategy_name

s = 'Momentum Strategy'
del s
# print(s)

s1 = "Singapore"
s2 = "India"
f = s1 +  " " + s2
print(sorted(f))

s1 = "Singapore"
s2 = "India"
print(sorted(s1))

s1 = "Singapore"
s2 = "India"
f = s1 + " " + s2
s1.capitalize()

s1 = "Singapore"
s2 = "India"
f = s1 + " " + s2
f
print("Hello world this is Kuldeep and i am from {} and currently i am working in {}".format(s2,s1))

s1 = "Singapore"
s2 = "India"
s3 = "123"
f = s1 + " " + s2 + " " + s3
print(f)
print(f.split("i"))

Join = "".join(['S', 'ngapore Ind', 'a 123'])
print(Join)

# Examples...

# Write a program which can remove a particular character from a string.
str = input("Enter the string: ")
new_str = ''
eliminate = input("enter the char you need to remove: ")
for i in str:
    if i != eliminate:
        new_str = new_str + i
print(new_str)


# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam
word = "malayalam"
l1 = []
for i in word:
    l1.append(i)
if l1[::] == l1[::-1]:
    print(f"the given word {word} is palindrome")


# Write a program to count the number of words in a string without split()
s = input('enter the string')
L = []
count = 0
temp = ''
for i in s:
  if i != ' ':
    temp = temp + i
    count += 1
  else:
      L.append(temp)
      temp = ''

print(count)


# Write a python program to convert a string to title case without using the title()
s = input('enter the string')

L = []
for i in s.split():
  L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))


# Write a program that can convert an integer to string.
number = int(input('enter the number'))

digits = '0123456789'
result = ''
while number != 0:
  result = digits[number % 10] + result
  number = number//10

print(result)
print(type(result))
