import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_choice = random.choice(cards)
dealer_choice = random.choice(cards)

print(f"Your starting card: {user_choice}")
print(f"Dealer's visible card: {dealer_choice}")

while True:
    again = input("Do you want to pick a card again? (y/n): ")

    if again == 'n':
        # Dealer keeps drawing until 17 or more
        while dealer_choice < 17:
            dealer_choice += random.choice(cards)

        print(f"Dealer's final total: {dealer_choice}")

        if dealer_choice > 21:
            print("Dealer busts! You win!")
        elif user_choice > dealer_choice:
            print(f"You win! Your total: {user_choice}, Dealer's total: {dealer_choice}")
        elif user_choice < dealer_choice:
            print(f"You lose! Your total: {user_choice}, Dealer's total: {dealer_choice}")
        else:
            print(f"It's a tie! Both have: {user_choice}")
        break

    elif again == 'y':
        new_card = random.choice(cards)

        # If adding an Ace (11) would bust, count it as 1
        if new_card == 11 and user_choice + 11 > 21:
            user_choice += 1
        else:
            user_choice += new_card

        print(f"You picked: {new_card}, your total is now: {user_choice}")

        if user_choice > 21:
            print("You bust! You lose.")
            break
    else:
        print("Invalid input, please enter 'y' or 'n'.")
