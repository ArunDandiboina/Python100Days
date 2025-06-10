import random
from my_module import PI, add

print(PI)
print(add(5, 3))  # Outputs: 8
print(random.randint(1, 100))  # Generates a random integer between 1 and 100
print(random.choice(["rock", "paper", "scissors"]))

# including both 0 and 1 in the range
if random.randint(0,1):
    print("Tails")
else:
    print("Heads")