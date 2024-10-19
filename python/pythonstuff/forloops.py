#all in same line

for x in range(1,11):
    print(x, end="")
print("woahhh")

#reversed

for x in reversed(range(1,11)):
    print(x)
print("woahhh")

for x in reversed(range(1,11,2)):
    print(x)
print("woahhh")

#print x in y

y = "1234-34134-1234-134"
for x in y:
    print(x)
print("woahhh")

#breaks

for x in range(1,21):
    if x == 1:
        continue
    else:
        print(x)
print("woahhh")

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)
print("woahhh")