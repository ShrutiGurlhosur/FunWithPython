import os

gavel_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ 
'''

bids = {}
users = "yes"

#accpet data from all the users
while users == "yes":
    os.system("clear")
    print(gavel_logo)

    while True:
        name = input("What's your name? : ").lower()
        #validation check for user name
        if  not str(name).isalpha():
            print("Please enter a valid name!")
            continue
        else:
            break

    bid_amount = float(input("What's your bid amount? :$"))

    #add user data to dictionary
    bids[name] = float(bid_amount)

    #validation check for user input
    while True:
        users = input("Are there anymore users? (yes/no): ")
        if users not in ["yes","no"]:
            print("You have entered an invalid choice.")
            continue
        else:
            break


max_bid = 0
max_bidder = ""
for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        max_bidder = bidder

print(f"\n\nThe winner is {max_bidder} with a bid of ${max_bid}\n\n")

