name = input("Enter full name: ")

result = len(name)
result1 = name.find("n") + 1
result2 = name.rfind("c") + 1
result3 = name.capitalize ()
result4 = name.upper ()
result5 = name.lower ()
result6 = name.isdigit () #all should be numbers
result7 = name.isalpha () #all should be alphabetical, no spaces
result8 = name.count("a") #counts all instances of "a"
result9 = name.replace("a", "b") #replaces "a" with "b"

print(f"Number of characters: {result}")
print(f"Finds (n): {result1}")  
print(f"Finds the last (c): {result2}")
print(f"Capitalize First Letter: {result3}")
print(f"Uppercased: {result4}")
print(f"Lowercased: {result5}")

import time

x = 'i want a thrill of a double life'
name = input("Enter full name: ")

result = len(name)

print(f'{result}')

for i in range (0, 10):
    print(f'{x}')
    time.sleep(0.2)

