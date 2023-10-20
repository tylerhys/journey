# You are going to write a program that calculates the sum of all the even numbers from 1 to X.
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for i in range(0,target+1):
  if i%2 == 0:
    sum += i

print(sum)
