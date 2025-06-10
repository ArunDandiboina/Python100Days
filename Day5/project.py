# password generator
import string
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

user_password = []

# print(numbers)
# print(symbols)
# print(letters)

import random

print("Welcome to the password generator!")
print("How many letters would you like in your password?")
num_letters = int(input())
print("How many symbols would you like in your password?")
num_symbols = int(input())
print("How many numbers would you like in your password?")
num_numbers = int(input())

for _ in range(num_letters):
    user_password.append(random.choice(letters))
for _ in range(num_symbols):
    user_password.append(random.choice(symbols))
for _ in range(num_numbers):
    user_password.append(random.choice(numbers))

random.shuffle(user_password)  # shuffle the password list to randomize order
final_password = ''.join(user_password)  # join the list into a string
print(f"Your password is: {final_password}")  # print the final password