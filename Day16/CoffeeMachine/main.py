# Coffee Machine Program
from menu import Menu
from coffee_maker import CoffeeMaker
from  money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    choice = input("What would you like? (espresso/latte/cappuccino) or 'report' to view resources, 'off' to exit: ").lower()
    found, drink = menu.find_drink(choice)
    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif not found:
        print("Sorry, that drink is not available. Please choose from the menu.")
    elif coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            print("Transaction failed. Please try again.")