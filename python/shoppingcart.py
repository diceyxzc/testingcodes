foods = []
prices = []
total = 0

while True:
    food = input("Enter you would buy(Q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of the {food}: ₱"))
        foods.append(food)
        prices.append(price)

print("----- YOUR GROCERIES -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price

print("")
print(f"Your total is: ₱{total}")