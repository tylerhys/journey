#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
INPATH_LETTER = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\24-Mail-Merger\\Input\\Letters\\starting_letter.txt"
INPATH_NAME = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\24-Mail-Merger\\Input\\Names\\invited_names.txt"

OUTPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\24-Mail-Merger\\Output\\ReadyToSend\\letter_for_"

with open(INPATH_LETTER) as letter:
    letter_template = letter.read()

with open(INPATH_NAME) as name:
    names = name.readlines()

namelist = []
for name in names:
    newname = name.strip()
    namelist.append(newname)

for name in namelist:
    letter_content = letter_template.replace("[name]",name)
    path = OUTPATH + name + ".txt"
    with open(path,"w") as letter:
        letter.write(letter_content)