capitals = {"Usa": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("Usa"))

capital = input("Enter a capital city: ")

if capital in capitals.values():
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"Usa": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#capitals.get()
#keys = capitals.keys()
#values = capitals.values()
#items = capitals.items()

#print(capitals)
#print(keys)
#for key in capitals.keys():
#    print(key)
#for value in capitals.values():
#    print(value)

#for key, value in capitals.items():
#    print(f"{key}: {value}")