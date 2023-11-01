name = "Tyler"

newlist = [letter for letter in name]
print(newlist)
# ['T', 'y', 'l', 'e', 'r']

newrange = [n*2 for n in range(1,10)]
print(newrange)
#[2, 4, 6, 8, 10, 12, 14, 16, 18]

l10range = [n for n in newrange if n < 10]
print(l10range)
# [2, 4, 6, 8]