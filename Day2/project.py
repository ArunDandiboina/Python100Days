# Tip calculator.

# welcome message
# what is the total bill?
# how much tip would you like to give?
# How many people to split the bill?

# 200 + 20% tip = 240
# 240 / 3 = 80

print("Welcome to the tiop calculator.")
total_bill = float(input("What is the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amount = round((total_bill + (total_bill * (tip_percentage / 100)))/ people, 2)
print(f"Each person should pay: ${amount}")
