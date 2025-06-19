import random
import os

# Data for the game - remains a global constant as it's static game data
data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 654_900_000,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 504_900_000,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 421_800_000,
        "description": "Singer, Actress, Entrepreneur",
        "country": "United States",
    },
    {
        "name": "Dwayne 'The Rock' Johnson",
        "follower_count": 394_900_000,
        "description": "Actor, Producer, Retired Wrestler",
        "country": "United States",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 394_400_000,
        "description": "Reality TV Star, Businesswoman",
        "country": "United States",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 376_400_000,
        "description": "Singer, Actress",
        "country": "United States",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 358_100_000,
        "description": "Reality TV Star, Businesswoman",
        "country": "United States",
    },
    {
        "name": "Beyoncé",
        "follower_count": 312_900_000,
        "description": "Singer, Actress, Businesswoman",
        "country": "United States",
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 304_300_000,
        "description": "Reality TV Star, Businesswoman",
        "country": "United States",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 295_000_000,
        "description": "Singer",
        "country": "Canada",
    },
]

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_celebrity(exclude_celeb=None):
    """
    Returns a random celebrity dictionary from the 'data' list.
    If 'exclude_celeb' is provided, ensures the returned celebrity is different from it.
    """
    chosen_celeb = random.choice(data)
    # Loop to ensure the new celebrity is not the same as the one we want to exclude
    while chosen_celeb == exclude_celeb:
        chosen_celeb = random.choice(data)
    return chosen_celeb

def format_celebrity_info(celeb_data):
    """
    Formats the celebrity's name, description, and country into a readable string.
    """
    return f"{celeb_data['name']}, a {celeb_data['description']}, from {celeb_data['country']}"

def check_guess(guess, celeb_a, celeb_b):
    """
    Compares the follower counts of celeb_a and celeb_b and checks if the user's
    guess ('A' or 'B') is correct.
    Returns True if the guess is correct, False otherwise.
    """
    if celeb_a['follower_count'] > celeb_b['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'

clear_screen()

def play_higher_lower():
    """
    Runs the 'Higher or Lower' game.
    The game continues as long as the user makes correct guesses.
    """
    score = 0
    game_should_continue = True

    # Get initial two distinct celebrities
    celeb_a = get_random_celebrity()
    celeb_b = get_random_celebrity(celeb_a)

    while game_should_continue:
        # You could add a game logo or title here if you have one
        # print(GAME_LOGO) # Example if you defined a logo constant

        print(f"Compare A: {format_celebrity_info(celeb_a)}")
        print(f"Against B: {format_celebrity_info(celeb_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if user_guess not in ('A', 'B'):
            print("Invalid input. Please type 'A' or 'B'.")
            # Continue the loop without penalty for invalid input
            continue

        is_correct = check_guess(user_guess, celeb_a, celeb_b)

        if is_correct:
            clear_screen()
            score += 1
            print(f"You're right! Current score: {score}")
            # For the next round, 'B' becomes 'A', and a new 'B' is chosen,
            # ensuring it's different from the new 'A'.
            celeb_a = celeb_b
            celeb_b = get_random_celebrity(celeb_a)
        else:
            clear_screen()
            print(f"Sorry, that's wrong! Final score: {score}")
            game_should_continue = False
    
    print("Game Over!")

# This ensures the game only runs when the script is executed directly
if __name__ == "__main__":
    play_higher_lower()