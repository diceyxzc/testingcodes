import math

x = 2.13
y = 3.14
z = 5
w = -8.31

#all sorts of arithmetics

round = round(x)
absolute = abs(w)
remainder = x % 2
power = pow(x, 3)
max = max(x, y, z, w)
min = min(x, y, z, w)

print(f"{absolute}")
print(f"{round}")
print(f"{remainder:.2f}")
print(f"{power:.2f}")
print(f"{max}")
print(f"{min}")
print("")

#more formats of 2 decimal places

print('Prints pi: {:.2f}'.format(math.pi))
print('Prints e: {:.2f}'.format(math.e))
print('Prints square root: {:.2f}'.format(math.sqrt(x)))
print("Prints rounded up:",math.ceil(x))
print("Prints rounded down:",math.floor(x))