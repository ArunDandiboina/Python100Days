class CoffeeMaker:
    ''' Models the machine that makes coffee '''
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        
    def report(self):
        """Prints a report of the current resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        
    def is_resource_sufficient(self, drink):
        """Check if there are enough resources to make the drink."""
        for item in drink.ingredients:
            if self.resources[item] < drink.ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True
    
    def make_coffee(self, drink):
        """Deducts the required ingredients from the resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")