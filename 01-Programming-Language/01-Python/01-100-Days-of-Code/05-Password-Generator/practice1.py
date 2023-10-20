# You are going to write a program that calculates the average student height from a List of heights.
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total = 0
# Write your code below this row 👇
for x in student_heights:
  total += x
num = len(student_heights)
average = round(total / num)
print(f"total height = {total}\nnumber of students = {num}\naverage height = {average}")