import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break

OUTPUT:
Guess a number between 1 and 100: 66
Too low!
Guess a number between 1 and 100: 908
Too high!
Guess a number between 1 and 100: 67
Too low!
Guess a number between 1 and 100: 67
Too low!
Guess a number between 1 and 100: 098
Correct! You guessed the number.
