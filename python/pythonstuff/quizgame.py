questions = ("Water or Lemonade?: ",
             "Cardi B or Cardi A?:",
             "Insanity or Crazy?: ")

options = (("A. Water", "B. Lemonade"),
           ("A. Cardi B", "B. Cardi A"),
           ("A. Insanity", "B. Crazy"))

answers = ("A", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A or B): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num = question_num + 1

print("-------------------")
print("      RESULTS      ")
print("-------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")