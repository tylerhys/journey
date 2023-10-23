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
    print(numOfA)
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
            print(i)
            pts2.append(pts1 + 1*i + 11*(numOfA-i))
        for i in pts2:
            if i <= 21 and i > pts:
                pts = i
            if pts == 0:
                pts2.sort()
                print(pts2)
                pts = pts2[0]
    return pts

player=["A","5","J"]
print(calcPts(player))