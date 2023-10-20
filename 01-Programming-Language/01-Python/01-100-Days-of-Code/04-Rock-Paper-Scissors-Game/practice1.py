# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random
result = random.randint(0,1)

if result == 1:
  print("Heads")
else:
  print("Tails")