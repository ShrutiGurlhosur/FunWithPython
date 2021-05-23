import string
import os

alphabet = list(string.ascii_lowercase)

caesar_logo = '''
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
'''

def caesar_cipher(direction,text,shift):
    cipher_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter.isalpha():
            cipher_text += alphabet[(alphabet.index(letter) + shift) % 26]
        else:
            cipher_text += letter

    return cipher_text




choice = "yes"
while choice == "yes" or choice[0] == "y":
    os.system("clear")
    print(caesar_logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode","decode"]:
        print("You have entered an invalid choice. Please press enter to continue.")
        _ = input("")
        continue
    text = input("Type you message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"Here's the {direction}ed result: {caesar_cipher(direction,text,shift)}\n")

    choice = input("Do you want to continue with more messages? (yes/no):\n")
print("Good Bye!")