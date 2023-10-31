file = open("01-Programming-Language\\01-Python\\01-100-Days-of-Code\\24-Mail-Merger\\my_file.txt",mode="r")
contents = file.read()
print(contents)
file.close()

with open("01-Programming-Language\\01-Python\\01-100-Days-of-Code\\24-Mail-Merger\\my_file.txt",mode="a") as file:
    file.write("\nNewLine")