from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
INPUT = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\data\\french_words.csv"
OUTPUT = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\data\\words_to_learn.csv"

word = {}
idx = 0
flipped = FALSE

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


img_card_front = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\images\\card_front.png")
img_card_back = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\images\\card_back.png")
img_right = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\images\\right.png")
img_wrong = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\31-Capstone-Flash-Card\\images\\wrong.png")

# -------------------------- WORD HANDLING ----------------------------- #

try:
    data = pandas.read_csv(OUTPUT)
except:
    data = pandas.read_csv(INPUT)
    data.to_csv(OUTPUT,index=None)
    print("words_to_learn.csv does not exist. It has been created.")


def get_word():
    global word
    global idx

    idx = randint(0,len(data)-1)
    word = {
        "french": data.French[idx],
        "english": data.English[idx]
    }

def update_word():
    global flipped

    if not flipped:
        canvas.itemconfig(text_word,text=word["english"])
    else:
        canvas.itemconfig(text_word,text=word["french"])

def next_word():
    global flipped

    if flipped:
        get_word()
        flip_card()
        window.after(3000,flip_card)

def right():
    global idx

    data.drop(index=idx,inplace=True)
    data.to_csv(OUTPUT,index=None)
    next_word()

# ---------------------------- AUTO FLIP ------------------------------ #
def flip_card():
    global flipped

    if  not flipped:
        canvas.itemconfig(card,image=img_card_back)
        canvas.itemconfig(text_lang,text="English",fill="white")
        update_word()

        flipped = TRUE
    else:
        canvas.itemconfig(card,image=img_card_front)
        canvas.itemconfig(text_lang,text="French",fill="black")
        update_word()

        flipped = FALSE


# ---------------------------- UI SETUP ------------------------------- #
## Flash Card
canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card = canvas.create_image(400,263,image=img_card_front)
get_word()
text_lang = canvas.create_text(400,150,text="French",fill="black",font=(FONT_NAME,40,"italic"))
text_word = canvas.create_text(400,263,text=word["french"],fill="black",font=(FONT_NAME,60,"bold"))

## Buttons
button_right = Button(image=img_right,highlightthickness=0,command=right)
button_wrong = Button(image=img_wrong,highlightthickness=0,command=next_word)

## UI Grid Setup
canvas.grid(column=0,row=0,columnspan=2)
button_right.grid(column=1,row=1)
button_wrong.grid(column=0,row=1)

window.after(3000,flip_card)

window.mainloop()