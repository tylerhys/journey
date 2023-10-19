# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
inputStr = str(two_digit_number)
output = int(inputStr[0]) + int(inputStr[1])
print(output)