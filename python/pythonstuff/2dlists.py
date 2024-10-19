fruits = ["apple", "pear", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)

print(groceries[0][0])

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()