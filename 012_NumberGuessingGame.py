import random
import os

logo = '''
 _______           _______  _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \ 
| (    \/| )   ( || (    \/| (    \/| (    \/
| |      | |   | || (__    | (_____ | (_____ 
| | ____ | |   | ||  __)   (_____  )(_____  )
| | \_  )| |   | || (            ) |      ) |
| (___) || (___) || (____/\/\____) |/\____) |
(_______)(_______)(_______/\_______)\_______)
'''

NUMBER = random.randint(1,100)

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def get_no_of_attempts(level):
    if level =="easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def guess_number(attempts):
    while attempts >0 :
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        attempts -= 1
        if guess == NUMBER:
            print("You guessed it!\nYou win!\n")
            return
        elif guess > NUMBER:
            print("Too High.\n")
        else:
            print("Too Low.\n")
    else:
        print(f"The number was {NUMBER}.\n")
        print("You exhausted all of your attempts. \nYou lose!\n")


os.system("clear")
print(logo)
print("I am thinking a number between 1 and 100.")
wrong_level = True

while wrong_level:
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level in ["easy","hard"]:
        wrong_level = False

attempts = get_no_of_attempts(level)
guess_number(attempts)