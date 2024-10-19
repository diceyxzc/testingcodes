for y in range(3):
    for x in range(1,10):
        print(x, end=" ")
    print()

rows = int(input("Enter # of rows: "))
columns = int(input("Enter # of columns: "))
symbol = input("Enter # of symbols: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()