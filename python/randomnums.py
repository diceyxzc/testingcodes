import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "K", "A"]

number = random.randint(low, high)
option = random.choice(options)
random.shuffle(cards)

print(number)
print(option)
print(cards)