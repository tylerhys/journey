# Congratulations, you've got a job at Python Pizza! 
# Your first job is to build an automatic pizza order program.

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
  bill = 15
elif size == "M":
  bill = 20
elif size == "L":
 bill = 25

if size == "S":
  if add_pepperoni == "Y":
    bill += 2
elif add_pepperoni == "Y":
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")