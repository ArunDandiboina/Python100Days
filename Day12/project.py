# utilize global, constants, local and functions.
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

number = random.randint(1, 100)

# Difficulty levels
# Easy: 10 attempts
# Hard: 5 attempts
def set_difficulty():
    level = input("Choose a difficulty level (easy/hard): ").strip().lower()
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Invalid choice, defaulting to easy level.")
        return EASY_LEVEL_ATTEMPTS

# check if the guess is too low, too high, or correct
def check_guess(guess, number):
    if guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You've guessed the number:", number)
        return True
    return False

# Main game function  
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    while True:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
            attempts -= 1
        else:
            print("Sorry, you've run out of attempts. The number was:", number)
            break
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if check_guess(guess, number):
            break

# Start the game 
game()
