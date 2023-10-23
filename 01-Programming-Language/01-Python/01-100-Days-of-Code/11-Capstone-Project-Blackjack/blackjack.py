import os
import art
import random

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cardvalue = {"A":11,"K":10,"Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
cards = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
end = False

def calcPts(player):
    pts = 0
    pts1 = 0
    pts2 = []
    numOfA = player.count("A")
    playertemp = player.copy()
    if numOfA == 0:
        for card in playertemp:
            pts += cardvalue[card]
        return pts
    else:
        for i in range(numOfA):
            playertemp.remove("A")
        for card in playertemp:
            pts1 += cardvalue[card]
        for i in range(numOfA+1):
            pts2.append(pts1 + 1*i + 11*(numOfA-i))
        for i in pts2:
            if i <= 21 and i > pts:
                pts = i
            if pts == 0:
                pts2.sort()
                pts = pts2[0]
    return pts



while not end:
    skip = False
    playerPts = 0
    compPts = 0
    
    conti = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ").lower()
    if conti == "n":
        end = True
    else:
        player = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
        computer = [cards[random.randint(0,12)],cards[random.randint(0,12)]]
        print(art.logo)
        
        while not skip:
            playerPts = calcPts(player)
            print(f"Your cards: {player}, current score: {playerPts}")
            print(f"Computer's first hand: [{computer[0]}]")
            takeCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if takeCard == "y":
                player.append(cards[random.randint(0,12)])
            else:
                skip = True
            
            if calcPts(player) > 21:
                playerPts = calcPts(player)
                skip = True
        
        if playerPts <= 21:
            compPts = calcPts(computer)

            while compPts <= playerPts:
                computer.append(cards[random.randint(0,12)])
                compPts = calcPts(computer)
            
            print(f"Your final hand: {player}, final score: {playerPts}")
            print(f"Computer's final hand: {computer}, final score: {compPts}")

            if compPts > 21:
                print("Computer went over! YOU WIN!!!")
            elif compPts == playerPts:
                print("Its a tie.")
            elif compPts < playerPts:
                print("You win!!!")
            elif compPts > playerPts:
                print("You lose...")
        else:
            print(f"Your final hand: {player}, final score: {playerPts}")
            print("You went over! YOU LOSE!!!")
        


        