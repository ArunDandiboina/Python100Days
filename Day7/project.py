import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
lives = 6
placeholder = '_' * len(word)
correct_guesses = set()

print("Welcome to the word guessing game!")
print(placeholder)

while True:
    display = ''

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    for letter in word:
        if letter == guess:
            display += letter
            correct_guesses.add(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += '_'

    print(display)
    
    if guess not in word:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives <= 0:
            print("You have run out of lives! Game over.")
            break

    print(f"Lives remaining: {lives}")

    if '_' not in display:
        print("Congratulations! You've guessed the word:", word)
        break
    