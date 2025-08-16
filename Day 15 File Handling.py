#trades.csv

#opening a file
f = open("trades.csv","w")
f.write("My name is Tushar bhatt and i m a student of nitk...")
f.close()

#Reading a file

content  = open("trades.csv",'r')
print(content.read(6))      #reading n number of characters
print(content.read())
content.close()

#Writing Multiline...
f1 = open("trades.txt", 'w')
f1.write("Hello world!!")
f1.write("\nIm Tushar Mars Citizen !\n\n")
f1.close()

#Writing Multiline using list...
f1 = open("trades.txt", 'w')
l = ["Hello world!!", "\nIm Tushar Mars Citizen123 !"]
f1.writelines(l)
f1.close()

f1 = open("trades.txt", 'r')
print(f1.read())
f1.close()
print()

#reading line one by one...
f2 = open("trades.txt","r")
print(f2.readline(),end="")
print(f2.readline())
f2.close()
print()


#using Loops for data access...
file = open("trades.txt", "r")
while True:
    data1 = file.readline()
    if data1 == "":
        break
    else:
        print(data1, end="")
file.close()

#Using Context Manager (WITH)...

with open("Hi.txt", "w") as f:
    f.write("Hello again this is Tushar Bhatt from NITK.")

#using Append
with open("Hi.txt", "a") as f:
    f.write("\nI made this statement while i was using the append function")

#Using CSV Files...
import csv
with open("trades.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["symbol", "price", "quantity"])
    writer.writerow(["AAPL", "123", "50"])
    writer.writerow(["MSST", "121", "10"])

with open("trades.csv", "r") as f:
    content = f.readlines()
    print(content)
