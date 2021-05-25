from BlackJackArt import logo
import random
import os

deck = [11,2,3,4,5,6,7,8,9,10,10,10]

def draw():
    return random.choices(deck,k=2)

def hit():
    return random.choice(deck)

def score(user):
    score = 0
    for hand in user:
        score += hand
        if hand == 11 and score >21 :
            score -= 10
    return score

def find_results(user,comp):
    if score(user) > 21:
        print("Busted! You lose!\n")
    elif(21 - score(user)) < (21 - score(comp)):
        print("You win!\n")
    elif score(user) == score(comp):
        print("It's a draw!\n")
    else :
        print("Computer Wins!")
        print("You lose!\n")

def is_winner(user):
    if score(user) > 21:
        return "Busted! You lose."
    elif score(user) == 21 :
        return "You win!"

should_continue = True

while should_continue:
    os.system("clear")
    print(logo)

    user = []
    comp = []

    is_game_over = False

    user = draw()
    print(f"Your cards: {user}, current score: {score(user)}")

    comp = draw()
    print(f"Computer's first card: {comp[0]}")

    if score(user) == 21 and len(user) == 2:
        print("BlackJack! You win!")
        is_game_over = True
    elif input("\nType 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        user.append(hit())
        print(f"You final hand: {user}, final score: {score(user)}\n")
        if score(user) >= 21:
            print(f"{is_winner(user)}\n")
            is_game_over = True


    if not is_game_over:
        if score(comp) < 17 :
            print(f"\nComputer's hand: {comp}, score: {score(comp)}\n")
            print("Computer's hand less than 17, dealer taking another card.\n")
            comp.append(hit())

        print(f"\nComputer's final hand: {comp}, final score: {score(comp)}\n")
        find_results(user,comp)

    if input("\nDo you want to play a game of BlackJack? Type 'y' or 'n' : ").lower() == 'n':
        should_continue = False