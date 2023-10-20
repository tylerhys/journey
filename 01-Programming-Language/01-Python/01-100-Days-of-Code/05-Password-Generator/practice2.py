# You are going to write a program that calculates the highest score from a List of scores.
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
high = 0
# Write your code below this row 👇
for i in range(0, len(student_scores)):
  if high <= student_scores[i]:
    high = student_scores[i]
    
print(f"The highest score in the class is: {high}")