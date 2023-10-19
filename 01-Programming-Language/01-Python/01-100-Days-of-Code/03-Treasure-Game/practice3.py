# Write a program that works out whether if a given year is a leap year.
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year%400 == 0:
  print("Leap year")
elif year%100 != 0:
  if year%4 == 0:
    print("Leap year")
  else:
    print("Not leap year")
else:
  print("Not leap year")