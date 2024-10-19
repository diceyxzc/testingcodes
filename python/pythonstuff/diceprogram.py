import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐",
"│         │",
"│         │",
"│         │",
"└─────────┘",

diceArt = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",),
}

dice = []
total = 0
numOfDice = int(input("How many dice?: "))

for die in range(numOfDice):
    dice.append(random.randint(1, 6))

#vertical
"""for die in range(numOfDice):
    for line in diceArt.get(dice[die]):
        print(line)"""

#horizontal
for line in range(5):
    for die in dice:
        print(diceArt.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"Total: {total}")