#name.

name = str(input("Enter your name:"))
while name == "":
    print("You did not enter your name...")
    name = str(input("Enter your name:"))
print(f"Congrats, {name}")

#string.

food = str(input("Enter a food you like(Q to quit.): "))
while not food.lower() == "q":
    print(f"You like the food {food}")
    food = str(input("Enter a food you like(Q to quit.): "))
print("alright")

#number.

num = int(input("Enter # between 1 - 10:"))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter # between 1 - 10: "))
print("alright")