# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height ** 2

if BMI < 18.5:
  result = "you are underweight."
elif BMI < 25:
  result = "you have a normal weight."
elif BMI < 30:
  result = "you are slightly overweight."
elif BMI < 35:
  result = "you are obese."
else:
  result = "you are clinically obese."

print(f"Your BMI is {BMI}, {result}")