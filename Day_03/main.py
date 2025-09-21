# Treasure Island Game
# https://www.draw.io/?lightbox=1&highlight=0000ff&editor=www.draw.io&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('Where do you want to go? '
                 'Type "left" or "right". ').lower()

if choice_1 == "right":
    print(r'''                      -     =    .--._
                    - - ~_=  =~_- = - `.  `-.
                  ==~_ = =_  ~ -   =  .-'    `.
                --=~_ - ~  == - =   .'      _..:._
               ---=~ _~  = =-  =   `.  .--.'      `.
              --=_-=- ~= _ - =  -  _.'  `.      .--.:
                -=_~ -- = =  ~-  .'      :     :    :
                 -=-_ ~=  = - _-`--.     :  .--:    D
                   -=~ _=  =  -~_=  `;  .'.:   ,`---'@
                 --=_= = ~-   -=   .'  .'  `._ `-.__.'
                --== ~_ - =  =-  .'  .'     _.`---'
               --=~_= = - = ~  .'--''   .   `-..__.--.
                 --==~ _= - ~-=  =-~_-   `-..___(  ===;
              --==~_==- =__ ~-=  - -    .'       `---'
      ''')
    print("Sonic got the treasure before you, try again.")

elif choice_1 == "left":
    print(r'''                _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      Lake with an Island
 ___.'       '.       /               '-._  
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-''')
    choice_2 = input('You\'ve come to a lake. '
                     'Type "wait" to wait for a boat '
                     'or\nType "swim" to swim across. ').lower()
    if choice_2 == "wait":
        print("Nice, you made it to the next level, you're pretty good at this!")
        print("Welcome to:")
        print(r'''
            _                                     _     _                 _ 
           | |                                   (_)   | |               | |
           | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
           | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
           | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
           \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
           ''')
        choice_3 = input("You arrive at the island unharmed. "
                         "There is house with 3 doors. One red, "
                         "one yellow and one blue. "
                         "\nWhich colour do you choose? ").lower()
        if choice_3 == "red":
            print("It's a room full of fire🔥. \nGame Over😞")
        elif choice_3 == "blue":
            print("You entered a room of beasts👹. \nGame Over😞")
        elif choice_3 == "yellow":
            print("You found the treasure😊. \nYou Win!🎉")
        else:
            print("You chose a door that doesn't exist. \nGame Over😞.")
    else:
        print(r'''
                    _,;_;/-",_
                 ,")  (  ((O) "  .`,
               ,` (    )  ;  -.,/;`}
             ,"  o    (  ( (  . -_-.
            `.  ;      ;  ) ) \`; \;
              `., )   (  ( _-`   \,'
                 "`'-,,`.jb
''')
        print("You got attacked by an angry Shark🐟. \nGame Over😞.")


else:
    print("You fell into a hole🕳. \nGame Over😞.")
