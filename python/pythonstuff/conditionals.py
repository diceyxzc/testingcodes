num1 = 5
num2 = 8
age = 19
status = str("Admin").lower()

print("Positive" if num1 > 0 else "Negative")
print("Even" if num2 % 2 == 0 else "Odd")
print(f"{num1}" if num1 > num2 else f"{num2}")
print("Adult" if age >= 18 else "Child")
print("Full Access" if status == str("admin") else "Cannot Grant Access")