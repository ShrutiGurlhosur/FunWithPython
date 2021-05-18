print('''Hobbit
              _,,,,_
           .(((()()()(
           ())()()))())
          ((,.""-,(()())
          \ @ ) @  )/)()
          .'-. -   (C))
          (  (_. ` .))
          \ .___.   .'
         __`.____.' \_____
       /(  " /))_\.-'  (  `\
      / ( _  o/(o "  _ \   `.
     (  /. . o)/o       (    \
    /   ( . o/(o .  "  .)\    )
   (   )( _ o)\o  _   . )(    )
   (   (.' o)/o    `.   )/   /
    \ ( . "o((o .  . ` _/   )
     (/)____o)/o______(c`-.)
      |)_|__[H]___|___(//)'
      (   )  : \  )    `''
      (_)  (  )    \ (_ )
      (      .   (      )
     (  ( )   (\  /  )  )
      (    (   (       )
      (  ( ) ./ \ ( .( )
       (     )  (     )
       |"^"")    ("^"")
       |    /    \    |
 pils  ),,,,)    |,,,,/
       /,,,,(    ),,,,(
    .-',,,,,)    /,,,,\
   ((((_).-'    (_)())))''')

print("Hello! I am Frodo Baggins of Bagend in Shire. Basically I am a Hobbit you see!\n")
print("I have been assigned this very strange and dangerous adventure by this wizard I know, Gandalf the Grey.\n")
print("He does the best fireworks in whole of the middle earth!\n")
print("You see, I hate adventures! It takes you away from your home and makes you late for dinner!\n")
print("But, I respect Gandalf and have decided to go on this adventure like my uncle Bilbo Baggins did once.\n")
print("The task I've been assigned with is to destroy this evil and powerful ring my uncle Bilbo has\n")
print("The challenge is, it can only be destroyed with fire of Mount Doom in Mordor,and I've never been outside Shire.\n")
print("I need your help to navigate to Mordor. Will you be my companion in this adventure?\n")
choice = input("Will you be my Samwise gamgee? (y/n) \n")
if choice == "n" or choice == "N":
    print("Ohh! Not everyone can bear this burden,I understand Sam!\n")
    print("Good Bye!\n")
    exit()
else:
    print("I knew you won't disappoint me  Sam!\n")
    choice = input ("Gandalf has asked us to meet us at Prancing Pony in Bree. Which way to go? (e, s )?\n")
    if choice == 's' or choice == 'S':
        print("we are in Old Forest. \n")
        print("we are attacked by ring wreaths!\n")
        print("Game Over\n")
        exit()
    else:
        print("we reached safely to Prancing Pony. \n")
        print("Now we'll wait for Gandalf. Wait the man in the corner who is called 'Strider' is staring at us.\n")
        print("Looks like he knows Gandalf and has idea about the mission\n")
        choice = input("Should we trust the Strider? (y/n)\n")
        if choice == 'n' or choice == 'N':
            print("we are attacked by ring wreaths!\n")
            print("Game Over!\n")
            exit()
        else:
            print("I think the Same! I think we can trust him as he just saved us from ring wreaths!\n")
            print("Now we are at, Astronomy tower and it's too late. We should rest here for the night.\n")
            print("Darn it! This fool of Pippin Took attracted ring wreaths with his stupidity.\n")
            print("we are attacked by ring wreaths!\n")
            print("I am hurt badly.\n")
            choice = input("Strider says,only Elves can save me and we have to go to Rivendell. do you trust him? (y/n)\n")
            if choice == 'n' or choice == 'N' :
                print("I couldn't recover from the attack injury\n")
                print("Now, I am dead.\n")
                print("Mission Failed! \n Game Over\n")
                exit()
            else:
                print("You saved my life by taking me to Rivendell Sam! \n")
                print("Thank you!\n")
                print("We have lost plenty time already. It's time to move.\n")
                choice = input('Which way to go? (e/w/s/n)\n')
                if choice == 'w' or choice == 'W':
                    print("You are going back home!\n")
                    print("you gave up!\n")
                    print("Misison Failed!\n")
                    print("Game Over!\n")
                    exit()
                elif choice == 'e' or choice == 'E':
                    print("Ohh no! We are in Goblin Town\n")
                    print("Goblin ate us and we are dead.\n")
                    print("Game Over!\n")
                    exit()
                elif choice == 'n' or choice == 'N':
                    print("Ohh no! We are in Gundabad!\n")
                    print("Goblin ate us and we are dead.\n")
                    print("Game Over!\n")
                    exit()
                else:
                    print("We reached Hollin Gate.\n")
                    print("I am already feeling heaviness of the ring. We have to move fast.\n")
                    choice = input('Which way to go? (e/w/s/n)\n')
                    if choice == 'w' or choice == 'W' :
                        print("You are going back home!\n")
                        print("you gave up!\n")
                        print("Misison Failed!\n")
                        print("Game Over!\n")
                        exit()
                    elif choice == 'e' or choice == 'E':
                        print("Ohh no! We are in Dol Guldur\n")
                        print("Goblin ate us and we are dead.\n")
                        print("Game Over!\n")
                        exit()
                    elif choice == 'n' or choice == 'N':
                        print("You are going back home!\n")
                        print("you gave up!\n")
                        print("Misison Failed!\n")
                        print("Game Over!\n")
                        exit()
                    else:
                        print("We reached Galadon.\n")
                        print("Sam, I feel ring is taking over me. We have to move fast.\n")
                        choice = input('Which way to go? (e/w/s/n)\n')
                        if choice == 'w' or choice == 'W':
                            print("You are going back home!\n")
                            print("you gave up!\n")
                            print("Misison Failed!\n")
                            print("Game Over!\n")
                            exit()
                        elif choice == 'e' or choice == 'E':
                            print("Ohh no! We are in Dol Guldur\n")
                            print("Goblin ate us and we are dead.\n")
                            print("Game Over!\n")
                            exit()
                        elif choice == 'n' or choice == 'N':
                            print("Ohh no! We are in Goblin town!\n")
                            print("Goblin ate us and we are dead.\n")
                            print("Game Over!\n")
                            exit()
                        else :
                            print("We reached Minas Tirith.\n")
                            print("Sam, I feel ring is taking over me. We have to move fast.\n")
                            choice = input('Which way to go? (e/w/s/n)\n')
                            if choice == 'w' or choice == 'W':
                                print("We are in Isengard\n")
                                print("Saruman bewitched us and gave ring to Sauron!\n")
                                print("Misison Failed!\n")
                                print("Game Over!\n")
                                exit()
                            elif choice == 's' or choice == 'S':
                                print("Ohh no! We are off the course\n")
                                print("Ring wreaths found us and we are dead.\n")
                                print("Game Over!\n")
                                exit()
                            elif choice == 'n' or choice == 'N':
                                print("Ohh no! We are in Dol Guldur!\n")
                                print("Goblin ate us and we are dead.\n")
                                print("Game Over!\n")
                                exit()
                            else:
                                print("We reached Osgiliath.\n")
                                print("Sam, I feel ring is taking over me. We have to move fast.\n")
                                print("Hey, Gollum finally is showing us way\n")
                                choice = input("Should we trust him? (y/n)\n")
                                if choice == 'n' or choice == 'N':
                                    print("Ohh No! Shelob spider of Minas Morgul ate us.\n")
                                    print("Game Over!\n")
                                    exit()
                                else:
                                    print("We finally reached our destination!\n")
                                    print("Ring is destroyed with Gollum!\n")
                                    print("Mission Successful!\n")
                                    print("Thank you Sawise Gamgee! You are a true  friend!\n")
                                    exit()

