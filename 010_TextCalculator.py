import os

logo = '''
 _____________________
|  _________________  |
| |  Python      0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

def add(num1,num2):
    """returns the summation of two numbers"""
    return num1+num2

def subtract(num1,num2):
    """returns the subtraction of two numbers"""
    return num1 - num2

def multiply(num1,num2):
    """returns the multiplication of two numbers"""
    return num1 * num2

def divide(num1,num2):
    """returns the division of two numbers"""
    return num1 / num2

operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

def calculator ():

    os.system("clear")
    print(logo)

    num1 = float(input("what's the first number?: "))

    choice = True

    while choice:
        for operator in operations:
            print(operator)

        symbol = input("\nselect the operator from above list: ")
        function = operations[symbol]

        num2 = float(input("\nWhat's the next number?: "))

        result = function(num1,num2)
        print(f"\n{num1} {symbol} {num2} = {result}\n")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit. : ").lower() == "y":
            num1 = result
        else:
            choice = False
            if input("Do you want to start a new calculation? (y/n): ").lower() == "y":
                calculator()
            else:
                exit(0)

calculator()