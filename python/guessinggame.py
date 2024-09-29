import random

lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)
guesses = 0
isrunning = True

print("|Python Number Guessing Game|")
print(f"Select a number between {lowestNum} and {highestNum}")

while isrunning:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowestNum or guess > highestNum:
            print("Out of range.")
            print(f"Select a number between {lowestNum} and {highestNum}")
        elif guess < answer:
            print("Too Low! Try again!")
        elif guess > answer:
            print("Too High! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}.")
            print(f"Number of guesses: {guesses}")
            isrunning = False
    else:
        print("Invalid guess.")
        print(f"Select a number between {lowestNum} and {highestNum}")