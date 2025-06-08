# logical operators definition - is used to combine conditional statements
# comparision operators - <, >, <=, >=, ==, !=
# logical operators - and, or, not

a = True
print(not a)

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("Can ride")
    age = int(input("What's your age? "))
    if age < 12:
        print("Child ticket: $5")
        bill = 5
    elif age <= 18:
        print("Youth ticket: $7")
        bill = 7
    elif age >= 45 and age <= 55:
        print("You get a free ride!")
        bill = 0
    else:
        print("Adult ticket: $12")
        bill = 12
    
    want_photo = input("Do you want a photo? yes or no ");
    if (want_photo == "yes"):
            bill += 3
    print(f"Your final bill is: ${bill}")        
else:
    print("Can't ride")