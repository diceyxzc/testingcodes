num1 = "1231-23111-3211"

#star : end : step

print(f"{num1[:4]}") #starting point
print(f"{num1[5:10]}")
print(f"{num1[5:]}")
print(f"{num1[-1]}") #last number
print(f"{num1[::2]}") #skips every nth number
print(f"{num1[::-1]}") #reverses

last4digits = num1[-4:]
print(f"{last4digits}")