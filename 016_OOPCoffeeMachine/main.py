from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_bin = MoneyMachine()


should_continue = True

while should_continue:
    choice = input("What do you want to do?(espresso/latte/cappuccino)? : ").lower()
    if choice not in ["espresso", "latte", "cappuccino", "stop", "report"]:
        print("You entered an invalid option. Enter again.")
        continue
    else:
        if choice == "stop":
            should_continue = False
        elif choice == "report":
            coffee_machine.report()
            print(f"Coffee Machine has: ${money_bin.profit}")
        else:
            drink = coffee_menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink) and money_bin.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
