# You are going to write a program that tests the compatibility between two people.
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = (name1 + name2).upper()
t1 = 0
t2 = 0
for i in range(len(name)):
  if name[i] == "T" or name[i] == "R" or name[i] == "U" or name[i] == "E":
    t1 += 1
  if name[i] == "L" or name[i] == "O" or name[i] == "V" or name[i] == "E":
    t2 += 1

score = int(str(t1) + str(t2))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")