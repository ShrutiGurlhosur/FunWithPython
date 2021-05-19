import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 

'''
paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors = '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \ 
|___/\___|_|___/___/\___/|_|  |___/

'''
options = [rock, paper, scissors]
user_choice = int(input("What do you choose? \nType 0 for Rock,\nType 1 for Paper,Type 2 for Scissors.\n"))
print (options[user_choice]+"\n\n")
print("Computer chose:\n")
comp_choice = random.randint(0,2)
print(options[comp_choice])
if user_choice == comp_choice:
    print("It's a Draw!\n")
elif user_choice > comp_choice:
    print ("You win!\n")
elif user_choice ==0 and comp_choice == 2:
    print ("you win!\n")
else:
    print("You lose!\n")
