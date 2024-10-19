import arithmeticoperations

obj = arithmeticoperations.Arithmetic()

num1 = int(input("Enter the Value of Number 1: "))
num2 = int(input("Enter the Value of Number 2: "))

sum = obj.get_sum(num1, num2)
difference = obj.get_difference(num1, num2)
product = obj.get_product(num1, num2)
quotient = obj.get_quotient(num1, num2)

print("Sum: ", sum)
print("Difference: ", difference)
print("Product: ", product)
print("Quotient: ", quotient)