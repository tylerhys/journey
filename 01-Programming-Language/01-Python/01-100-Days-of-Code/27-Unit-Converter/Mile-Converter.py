from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20,pady=20)

input = Entry(width=7)
t_Miles = Label(text="Miles")
t_eq = Label(text="is equal to")
t_output = Label(text="0")
t_KM = Label(text="KM")

def mileToKm ():
    t_output["text"] = int(input.get()) * 1.60934

button = Button(text="Calculate",command=mileToKm)

input.grid(column=1,row=0)
t_Miles.grid(column=2,row=0)
t_eq.grid(column=0,row=1)
t_output.grid(column=1,row=1)
t_KM.grid(column=2,row=1)
button.grid(column=1,row=2)
window.mainloop()