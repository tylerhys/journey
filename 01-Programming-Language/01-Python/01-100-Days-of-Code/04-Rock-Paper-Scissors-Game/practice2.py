# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

import random
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
randomName = names[random.randint(0,len(names)-1)]
print(randomName + " is going to buy the meal today!")