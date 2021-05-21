import random
import os

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#hangman word list
word_list = ["angel","baboon","breakfast","cranberry","drive","elephant","family","gameboy","houshold"]
lives = 6

print(logo)
print("\n\n\n")
#chosing a random word from list to guess from
chosen_word = random.choice((word_list))

#list to show blanks and to show progress
display = []
for _ in chosen_word:
    display.append("_")

#list to store invalid guesses
invalid_list = []

print(stages[len(stages)-lives-1])
print(f"{' '.join(display)}\n\n")

while "_" in display and lives > 0:

    #take guess input form user
    guess = input("Guess a letter:\n").lower()

    os.system("clear")

    #check for guessed letter
    #if user already guessed the character previously
    if not str(guess).isalpha():
        print("Please enter only alphabets (a-z)\n")
    elif guess in display:
        print("You already guessed that letter.\n")
    # if guessed char is invalid and already been guesses before
    elif guess in invalid_list:
        print("You already guessed that letter which is invalid.\n")
    # if guessed char is not present in chosen word
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        invalid_list.append(guess)
        lives -= 1
        #user exhausted all chances and lost
        if lives == 0:
            print(stages[len(stages)-lives-1])
            print(f"{' '.join(display)}\n\n")
            print(f"Word was: {chosen_word}")
            print("You lose!")
            exit(0)
    #character is present in chosen word
    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

    print(stages[len(stages) - lives-1])
    print(f"{' '.join(display)}\n\n")

print ("You win!\n\n")