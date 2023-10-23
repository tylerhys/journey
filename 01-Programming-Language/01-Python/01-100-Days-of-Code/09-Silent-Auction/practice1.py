# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades that 
# should contain student names for keys and their grades for values.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}

for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = "Outstanding"
  elif student_scores[key] >= 81:
    student_grades[key] = "Exceeds Expectations"
  elif student_scores[key] >= 71:
    student_grades[key] = "Acceptable"
  elif student_scores[key] <= 70:
    student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)