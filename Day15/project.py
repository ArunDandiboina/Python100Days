# coffee machine

# Expresso - 1.50, Latte - 2.50, Cappuccino. - 3.00
# 50ml w, 18g coff,( 200ml w, 24g cof, 150ml mil, (250mlw, 24g cof, 100ml mil

# resources - water 300ml, milk 200ml, coffee 100g

# coin operated - 1cent - 0.01, 5 cents - 0.05, 
# 10 cents - 0.10, 25 cents - 0.25, 

# dictionary for menu items

# report

# latte
# is_rescources_sufficient
# insert coins - quarters, dimes, nickels, pennies
# process_coins - if not sufficient, return coins, elif give change
# check_transaction
# make_coffee - deduct resources, return coffee

# Menu
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,  # Espresso does not require milk
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.00,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
# resouces_check
def is_resources_sufficient(drink):
    """Check if there are enough resources to make the drink."""
    for item in menu[drink]["ingredients"]:
        if resources[item] < menu[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def report():
    """Print the current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")
    
    
# process coins
def process_coins():
    """Process the coins inserted by the user."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    
    if total < menu[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += menu[drink]["cost"]
        change = total - menu[drink]["cost"]
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True

# make_coffee
def make_coffee(drink):
    """Deduct the resources needed for the drink."""
    for item in menu[drink]["ingredients"]:
        resources[item] -= menu[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!") 
   

while True:
    drink = input("What would you like? (espresso/latte/cappuccino) or 'report' to view resources, 'off' to exit: ").lower()
    if drink == "off":
        print("Turning off the coffee machine. Goodbye!")
        break
    elif drink == "report":
        report()
    elif drink not in menu:
        print("Invalid choice. Please choose from espresso, latte, or cappuccino.")
    elif is_resources_sufficient(drink):
        if process_coins():
            make_coffee(drink)
        else:
            print("Transaction failed. Please try again.")