import os
import art

auctionEnd = False

while not auctionEnd:
    print(art.logo)
    print("Welcome to the secret auction program.\n")
    name = input("What is your name?\n")
    bid = int(input ("What's your bid?\n"))
    conti = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    bidders = []
    participant= {}
    participant["name"] = name
    participant["bid"] = bid
    highestBid = 0
    winner = ""

    bidders.append(participant)

    if highestBid < bid:
        highestBid = bid
        winner = name
    
    if conti == "no":
        auctionEnd = True
    
    os.system('cls')


print(f"The winner is {winner} with a bid of ${highestBid}")