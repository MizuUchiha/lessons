
# guess_the_number_game.py
import random

number_to_guess = random.randint(1, 20)
attempts = 0

print("I am thinking of a number between 1 and 20.")

while attempts < 6:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Your guess is too low.")
    elif guess > number_to_guess:
        print("Your guess is too high.")
    else:
        break

if guess == number_to_guess:
    print(f"Good job! You guessed my number in {attempts} guesses!")
else:
    print(f"Nope. The number I was thinking of was {number_to_guess}")
