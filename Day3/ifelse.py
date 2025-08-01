# using modulo operator

# num = int(input("Enter a number: "))
num = 10  # Example number, you can change this to test

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# nested if else and elif statements.
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("Can ride")
    age = int(input("What's your age?"))
    if age < 12:
        print("Child ticket: $5")
        bill = 5
    elif age <= 18:
        print("Youth ticket: $7")
        bill = 7
    else:
        print("Adult ticket: $12")
        bill = 12
    
    want_photo = input("Do you want a photo? yes or no ");
    if (want_photo == "yes"):
            bill += 3
    print(f"Your final bill is: ${bill}")        
else:
    print("Can't ride")
