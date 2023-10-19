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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You are at a cross roads. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == "left":
    choice2 = input("You reach a huge lake with an island in the middle. Type 'wait' to wait for a raft. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You reached the island and 3 magical doors appear. Which door do you go through? 'Yellow','Blue' or 'Red'?\n").lower()
        if choice3 == "yellow":
            print("Congratulations! You have found the hidden treasure!")
        elif choice3 == "blue":
            print("You enter through the Blue door and are greeted by a Giant Ogre...\nIt's lunch  time...\nGAME OVER!!!")
        elif choice3 == "red":
            print("You enter through the Red door and immediately fall into a pit of lava...\nGAME OVER!!!")
        else:
            print("Not a valid choice...\nThe Game Master snaps you out of existence...\nGAME OVER!!!")
    else:
        print("Attacked by pirahnas. GAME OVER!!!")
else:
    print("Fall into a hole. GAME OVER!!!")