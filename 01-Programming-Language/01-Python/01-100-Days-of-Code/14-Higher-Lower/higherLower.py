import art
import game_data
import random
import os

end = False
pts = 0

def randomSelect():
    return random.randint(0,len(game_data.data)-1)

print(art.logo)
while not end:
    A = randomSelect()
    B = randomSelect()

    while B == A:
        B = randomSelect()
    
    if game_data.data[A]["follower_count"] < game_data.data[B]["follower_count"]:
        answer = "B"
    else:
        answer = "A"

    
    print(f"Compare A: {game_data.data[A]["name"]}, a {game_data.data[A]["description"]} from {game_data.data[A]["country"]}")
    print(art.vs)
    print(f"Compare B: {game_data.data[B]["name"]}, a {game_data.data[B]["description"]} from {game_data.data[B]["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B'\n").upper()
    
    os.system('cls')
    print(art.logo)
    if choice == answer:
        pts += 1
        print(f"You're correct! Current score: {pts}")
    else:
        end = True
        print(f"Sorry, that is the wrong answer. Final score: {pts}")

