# Rock paper and scissors.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = ''' 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

import random
l = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# if and elif only wins of user else - # computer wins
if user_choice < 0 or user_choice > 2:
    print("Invalid choice! Please choose 0, 1, or 2.")
elif user_choice == 1 and computer_choice == 0:
    print("\nYou chose Paper:" + paper)
    print("Computer chose Rock:" + rock)
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("\nYou chose Scissors:" + scissors)
    print("Computer chose Paper:" + paper)
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print("\nYou chose Rock:" + rock)
    print("Computer chose Scissors:" + scissors)
    print("You win!")
elif user_choice == computer_choice:
    print("\nYou chose:" + l[user_choice])
    print("Computer chose:" + l[computer_choice])
    print("It's a draw!")
else:
    print("\nYou chose:" + l[user_choice])
    print("Computer chose:" + l[computer_choice])
    print("You lose!")
