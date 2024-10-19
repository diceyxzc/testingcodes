#collection | when adding smt
fruits = ["apple", "orange", "banana", "coconut"]
fruits[0] = "pear"
fruits.append("pineapple")
fruits.remove("pear")
fruits.insert(2, "doughnut")
fruits.sort()
fruits.reverse()
fruits.index("apple")
fruits.clear("apple")
fruits.count("apple")

print(fruits)
print(fruits[::-1])

for fruit in fruits:
    print(fruit, end=" ")

print("")
print(len(fruits))
print("pineapple" in fruits)

#set | unordered | no duplicates
fruits = {"apple", "orange", "banana", "coconut"}
fruits.add("pineapple")
fruits.pop()
fruits.clear()

print(fruits)

#tuple | constants
fruits = {"apple", "orange", "banana", "coconut"}
fruits.add("pineapple")
fruits.pop()
fruits.clear()

print(fruits)

fruits = ("apple", "orange", "banana", "coconut")
fruits.index("apple")
fruits.count("orange")

print(fruits.index("apple"))
for fruit in fruits:
    print(fruit)