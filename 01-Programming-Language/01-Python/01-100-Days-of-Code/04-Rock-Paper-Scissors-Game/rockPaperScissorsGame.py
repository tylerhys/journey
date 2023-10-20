rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice < 0 or choice > 2:
    print("Not a valid input...")
else:
    computer = random.randint(0,2)

    rps=[rock,paper,scissors]
    print(f"You chose:\n{rps[choice]}")
    print(f"Computer chose:\n{rps[computer]}")

    if choice == computer:
        print("Its a tie!")
    elif choice == 0 and computer == 2:
        print("You win!")
    elif choice < computer or (choice == 2 and computer == 0):
        print("You lose!")
    else:
        print("You win!")