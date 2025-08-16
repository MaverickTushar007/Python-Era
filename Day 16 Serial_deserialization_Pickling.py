with open("hi.txt", "w") as f:
    f.write("1. My name Is Tushar Bhatt...")
    f.write("\n2. My name Is Tushar Bhatt...")
    f.write("\n3. My name Is Tushar Bhatt...")
    f.write("\n4. My name Is Tushar Bhatt...")
    f.write("\n5. My name Is Tushar Bhatt...")

with open("hi.txt",'r') as f:
    print(f.read())
print()

#Seek AND Tell...
with open("hi.txt",'r') as f:
    print(f.read(10))
    print(f.tell())
    print(f.read(10))
    print(f.tell())
    print(f.read(10))
print()

with open("hi2.txt",'w') as f:
    (f.write("1. hello my name is tushar bhatt and i study in clg"))
    print(f.tell())
    (f.seek(10))
    f.write("\n2. hello my name is tushar bhatt and i study in clg")

with open("hi2.txt",'r') as f:
    print(f.read())


#working with binary files...
with open("friend.png", "rb") as b:
    with open("new_friend.png", "wb") as g:
        g.write(b.read())

#Accessing Int and Dict:
with open("int.txt", "w") as f:
    # f.write(5)
    f.write("5")

d = {
    "name": "Tushar",
    "clg": "NITK"
}
with open("dict.txt", "w") as f:
    # f.write(d)
    f.write(str(d))

with open("dict.txt", "r") as f:
    print(f.read())
with open("int.txt", "r") as f:
    print(f.read())

#Serialization...
import json
l = [
     {
         "Name": "Tushar",
         "clg": "NITK"
     },
     {
         "Dept": "Chemical Engineering",
         "Roll No.": "241CH052"
     }
]

with open("trade_logs.json", "w") as f:
    json.dump(l,f)
with open("trade_logs.json","r") as f:
    print(json.load(f))

class TradeSystem:
    def __init__(self, tradeId, symbol, price, volume):
        self.tradeId = tradeId
        self.symbol = symbol
        self.price = price
        self.volume = volume

def show_object(obj):
    if isinstance(obj, TradeSystem):
        return f"the tradeId is {tradeObj.tradeId} for the symbol {tradeObj.symbol} @ price {tradeObj.price} for qt {tradeObj.volume}"

tradeObj = TradeSystem("T342", "AAPL", 100, 2000)

import json
with open("obj.json", "w") as f:
    json.dump(tradeObj,f, default = show_object)

#Deserialization...
with open("obj.json", "r")as f:
    d = (json.load(f))
    print(d)
    print(
        type(d)     #again the string type is what we have got!!!   Deseerialization didnt happen
    )

#pickling...
import pickle
with open("pickle_demo.pkl", "wb") as f:
    pickle.dump(tradeObj, f)

with open("pickle_demo.pkl", "rb") as f:
    data = (pickle.load(f))

print()
print(data.symbol)
print(data.volume)
print(data.price)
print(data.tradeId)