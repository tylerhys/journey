import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    output = ""
    if (direction == "decode"):
        shift *= -1
    for letter in text:
        if alphabet.__contains__(letter):
            output += alphabet[(alphabet.index(letter) + shift)%26]
        else:
            output += letter
    print(f"The {direction}d text is {output}")

repeat = True

while repeat:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    reply = input("Would you like to restart? Type Yes or No\n").lower()
    if reply == "no":
        repeat = False
    else:
        os.system('cls')