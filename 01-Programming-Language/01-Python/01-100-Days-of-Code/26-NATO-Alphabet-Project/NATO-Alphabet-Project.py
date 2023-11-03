import pandas

# INPATH = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\26-NATO-Alphabet-Project\\nato_phonetic_alphabet.csv"
INPATH = "nato_phonetic_alphabet.csv"
data = pandas.read_csv(INPATH)

#create dict {"A":"Alpha",...,}
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}

# list of letter from input of word
def get_phonetic():
    word = [letter for letter in input("Enter a word: ").upper()]
    try:
        nato_word = [nato_dict[letter] for letter in word ]
    except KeyError:
        print("Sorry, only letters in the alphabet please...")
        get_phonetic()
    else:   
        print(nato_word)

get_phonetic()