operator = input("Enter Operation: ").lower()
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

if (operator == str("add") or operator == str("+")):
    result = num1 + num2
elif (operator == str("subtract") or operator == str("-")):
    result = num1 - num2
elif (operator == str("multiply") or operator == str("*")):
    result = num1 * num2
elif (operator == str("divide") or operator == str("/")):
    result = num1 / num2
else:
    print("Invalid operator.")

print(f"{result}")