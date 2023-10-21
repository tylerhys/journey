#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ezpw = ""
for x in range(0,nr_letters):
    ezpw += letters[random.randint(0,len(letters)-1)]

for x in range(0,nr_symbols):
    ezpw += symbols[random.randint(0,len(symbols)-1)]

for x in range(0,nr_numbers):
    ezpw += numbers[random.randint(0,len(numbers)-1)]

print(f"Here is your password:\n{ezpw}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pw = ""
temp = ezpw

for i in range(0,len(ezpw)):
    pos = random.randint(0,len(temp)-1)
    pw += temp[pos]

    if len(temp) == 1:
        temp = temp
    elif pos == 0:
        temp = temp[slice(1,len(temp))]
    elif pos == (len(temp)-1):
        temp = temp[slice(0,len(temp)-1)]
    else:
        temp = temp[slice(0,pos)] + temp[slice(pos+1,len(temp))]
    # Check randomness    
    # print(f"i = {i}\npos = {pos}\npw = {pw}\ntemp = {temp}\n")

print(f"For better security, we randomised the positions:\n{pw}")

