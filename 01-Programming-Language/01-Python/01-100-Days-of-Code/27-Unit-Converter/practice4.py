from tkinter import *

## Window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

## Labels
my_label = Label(text="I am a label",font=("Arial",24,"bold"))
# my_label.pack()
# my_label.place(x=120,y=120)
my_label["text"] = "new text"
my_label.config(padx=10,pady=10)

## Buttons
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="click me",command=button_clicked)
button2 = Button(text="click me2",command=button_clicked)
# button.pack()

## Entry
input = Entry(width=10)
# input.pack()

## Using grid to position elements
my_label.grid(column=0,row=0)
button.grid(column=1,row=1)
input.grid(column=4,row=3)
button2.grid(column=2,row=0)


window.mainloop()

