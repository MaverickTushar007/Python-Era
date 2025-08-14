"""
1. Complex String Manipulation with Loops
Question: Given a string of mixed data containing symbols and prices like "AAPL100GOOG200MSFT300", write a script to
extract and print each symbol with its corresponding price on separate lines.
"""

data = "AAPL100GOOG200MSFT300"
ticker = ""
price = ""
i = 0

while i < len(data):
    # Extract the ticker (letters)
    ticker = ""
    while i < len(data) and data[i].isalpha():
        ticker += data[i]
        i += 1

    # Extract the price (digits)
    price = ""
    while i < len(data) and data[i].isdigit():
        price += data[i]
        i += 1

    # Print the pair
    print(f"{ticker} @ {price}")


"""
2. Using Break and Continue in Data Cleaning (This topic is covered in the next session 4)
Question: You are processing log data from trades. Stop processing if you encounter "ERROR" in the logs and skip 
any logs that start with "#".
"""

logs = [
    "# This is a comment",
    "TRADE: AAPL 150@100",
    "TRADE: MSFT 200@120",
    "ERROR: Connection lost",
    "TRADE: GOOG 100@130"
]

for log in logs:
    if log.startswith("#"):
        continue  # skip this log
    if "ERROR" in log:
        print("Error found, stopping log processing.")
        break
    print("Processing:", log)


"""
3. String Slicing and Indexing
Question: Given a long string of security transaction details formatted as "Buy100AAPLSell200GOOG", where each 
segment starts with a transaction type followed by the amount and the ticker, print each transaction detail 
on a new line.
"""
#ques 3 is kinda similar

"""
4. Nested Loops with String Functions
Question: Create a nested loop that reads a string of stock symbols separated by commas, then prints each symbol 
and its reverse.
"""
name = "AAPL, MSFT, TSLA, BTC"
lst = name.split(",")

for symbol in lst:
    rev_lst = ""
    for i in range(len(symbol)-1,-1,-1):
        rev_lst = rev_lst + symbol[i]
    print(f"{symbol} --->{rev_lst}")


"""
5. Advanced String Manipulation
Question: Given a block of text representing a financial report, replace any instance of financial terms with their 
uppercase counterparts. The terms are "revenue", "cost", "profit".
"""

report = """
The revenue increased in Q2. However, the cost of production also rose.
Our net profit was slightly better than expected.
"""
new = []
report_split = report.split()
for i in report_split:
    if i == "revenue" or i == "cost" or i == "profit":
        updated = (i.upper())
        new.append(updated)
    else:
        new.append(i)

print(new)
new_str = " ".join(new)
print(new_str)


"""
6. String Parsing and Control Flow
Question: Parse a string "High: 100, Low: 90, Open: 95, Close: 98" and print each value only if it is higher than 95.
"""
diction = []
price_info = "High: 100, Low: 90, Open: 95, Close: 98"
divide1 = price_info.split(",")
for i in divide1:
    divide2 = i.split(": ")
    if int(divide2[1]) > 95:
        print(f"{divide2[0]} : {divide2[1]}")
print(divide1)


"""
7. Advanced String Processing
Question: Convert a string representation of an options trade from "Call100AAPL20240101Put200GOOG20240102" into a 
structured report indicating each trade's type, volume, symbol, and date.
"""

todo = "Call100AAPL20240101Put200GOOG20240102"
i = 0
while i< len(todo):
    trade_type = ""
    if todo[i:i+4] == "Call":
        trade_type = "Call"
        i+=4                    #How many terms have been extracted at once!
    elif todo[i:i+3] == "Put":
        trade_type = "Put"
        i+=3
    else:
        i+=1
        continue
    #volume Extraction
    volume = ""
    while i< len(todo) and todo[i].isdigit():
        volume += todo[i]
        i += 1

    #extracting Symbol...
    symbol = ""
    while i< len(todo) and todo[i].isupper() and todo[i].isalpha():
        symbol += todo[i]
        i += 1

    date = todo[i:i+8]
    i+=8

print(
    f"Trade Type: {trade_type}, "
    f"symbol: {symbol}, "
    f"volume: {volume}, "
    f"date: {date} "
)
