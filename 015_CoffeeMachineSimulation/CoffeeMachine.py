from Menu import MENU
from Resources import resources

MONEY = 0.0

def show_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${MONEY}")

def is_sufficient_ingredients(coffee_type):
    is_sufficient = True

    req_water = MENU[coffee_type]["ingredients"]["water"]

    #Check for water level
    if req_water > resources["water"]:
        #is_sufficient = False
        #return is_sufficient
        return "Sorry, theres is not enough water."

    #check for milk level
    if coffee_type != "espresso":
        req_milk = MENU[coffee_type]["ingredients"]["milk"]

        if req_milk > resources["milk"]:
            #is_sufficient = False
            #return is_sufficient
            return "Sorry, theres is not enough milk."

    #check for coffee level
    req_coffee = MENU[coffee_type]["ingredients"]["coffee"]
    if req_coffee > resources["coffee"]:
        #is_sufficient = False
        #return is_sufficient
        return "Sorry, theres is not enough coffee."

    return "sufficient"



def brew_coffee(coffee_type):
    if coffee_type != "espresso":
        req_milk = MENU[coffee_type]["ingredients"]["milk"]
        resources["milk"] -= req_milk
    req_water = MENU[coffee_type]["ingredients"]["water"]
    req_coffee = MENU[coffee_type]["ingredients"]["coffee"]
    resources["water"] -= req_water
    resources["coffee"] -= req_coffee
    return f"Here's your {coffee_type}. Enjoy!"


def make_coffee(coffee_type):
    ingredients = is_sufficient_ingredients(coffee_type)
    if "sufficient" in ingredients:
        cost = MENU[coffee_type]["cost"]
        change = make_transaction(cost)
        if "change" in change:
            coffee = brew_coffee(coffee_type)
            return change+"\n"+coffee
        else:
            return change
    else:
        return ingredients



def make_transaction(cost):
    global MONEY
    change = 0
    print("Please insert coins.")
    quart = int(input("How many quarters? : "))
    dime = int(input("How many dimes? : "))
    nickel = int(input("How many nickels? : "))
    penny = int(input("How many pennies? : "))
    inserted_amt = (quart * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    if cost > inserted_amt:
        msg = "Sorry, that's not enough money. Money refunded."
    else:
        MONEY = MONEY + cost
        change = inserted_amt - cost

        msg = f"Here's your ${round(change,2)} in change."
    return msg


should_continue = True
while should_continue:

    coffee_type = input("What ☕️ would you like?️ (espresso/latte/cappuccino): ")
    if coffee_type not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("You entered invalid option. Please select a valid ☕️ option.\n")
        continue
    elif coffee_type == "off":
        should_continue = False
    elif coffee_type == "report":
        show_report()
    else:
        print(make_coffee(coffee_type))