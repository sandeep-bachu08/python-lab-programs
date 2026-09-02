import random

number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")