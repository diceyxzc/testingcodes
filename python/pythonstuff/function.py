def happyBirthday(name, age):
    print(f"Happy Birthday to you! {name} {age}")

happyBirthday("Insanity", 20)
happyBirthday("Steve", 40)
happyBirthday("Alex", 30)

print("")
def displayInvoice(username, amount, dueDate):
    print(f"Hello {username}")
    print(f"Your bill of ₱{amount:.2f} is due: {dueDate}")

displayInvoice("Alex", 21.3484, "September 29, 2024")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))

def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

fullName = createName("charise", "calvin")

print(fullName)