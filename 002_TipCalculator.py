print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n $"))
tip = 1 + (float(input("What percent tip would you like to give? 10, 12, or 15?\n")) /100)
No_people = int(input("How many people to split the bill?\n"))
print(f"Each person should pay: {(bill *tip)/No_people}")