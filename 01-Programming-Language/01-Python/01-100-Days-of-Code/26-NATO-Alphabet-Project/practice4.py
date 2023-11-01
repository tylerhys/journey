with open("01-Programming-Language\\01-Python\\01-100-Days-of-Code\\26-NATO-Alphabet-Project\\file1.txt") as file:
  file1 = file.readlines()

with open("01-Programming-Language\\01-Python\\01-100-Days-of-Code\\26-NATO-Alphabet-Project\\file2.txt") as file:
  file2 = file.readlines()

result = [int(n) for n in file1 if n in file2]

# Write your code above 👆
print(result)
