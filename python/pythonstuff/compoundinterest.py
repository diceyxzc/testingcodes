#this itteration does NOT allow 0

"""principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Principle is below or equal to 0.")

while rate <= 0:
    rate = float(input("Enter a interest rate: "))
    if rate <= 0:
        print("Interest rate is below or equal to 0.")

while time <= 0:
    time = float(input("Enter a time in years: "))
    if time <= 0:
        print("Time is below or equal to 0.")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time:.0f} years: ₱{total:,.2f}")"""

#this itteration allows 0

while True:
    principle = float(input("Enter a principle amount: "))
    if principle < 0:
        print("Principle is below 0.")
    else:
        break

while True:
    rate = float(input("Enter a interest rate: "))
    if rate < 0:
        print("Interest rate is below 0.")
    else:
        break

while True:
    time = float(input("Enter a time in years: "))
    if time < 0:
        print("Time is below 0.")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time:.0f} years: ₱{total:,.2f}")