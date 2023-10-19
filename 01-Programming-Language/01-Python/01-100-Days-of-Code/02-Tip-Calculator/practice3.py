# Create a program using maths and f-Strings that tells us how many weeks we have left.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
week = (90 - int(age)) * 52
print(f"You have {week} weeks left. ")