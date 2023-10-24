import art
import random
import os

print(art.logo)
print(
    """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
"""
)

answer = random.randint(1,100)
end = False
difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
print(f"Pssst, the correct answer is {answer}")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while not end:
    guess = int(input("Make a guess: "))
    if guess == answer:
        end = True
        print(f"You got it! The answer was {answer}")
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")

    attempts -= 1
    if attempts > 0 and not end:
        print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
    elif attempts == 0:
        end = True
        print("You've run out of guesses. You LOSE!!!")