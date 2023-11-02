from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timertext,text="00:00")
    title.config(text="Timer",fg=GREEN)
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    reps += 1

    work_sec = WORK_MIN 
    short_break_sec = SHORT_BREAK_MIN 
    long_break_sec = LONG_BREAK_MIN 

    if reps % 8 == 0:
        time = long_break_sec
        title.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        time = short_break_sec
        title.config(text="Break", fg=PINK)
    else:
        time = work_sec
        title.config(text="Work", fg=GREEN)

    countdown(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps

    min = math.floor(count / 60)
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timertext,text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count - 1)
    else:
        starttimer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark +="✔"
            check.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



## Tomato
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\28-Pomodoro-App\\tomato.png")
canvas.create_image(100,112,image=tomato)
timertext = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

## TIMER Text
title = Label(text="Timer",fg=GREEN,bg=YELLOW, highlightthickness=0,font=(FONT_NAME,40,"bold"))

## Button
start = Button(text="Start",command=starttimer)
reset = Button(text="Reset",command=reset)

## Check Markers
check = Label(fg=GREEN,bg=YELLOW, highlightthickness=0,font=(FONT_NAME,20,"bold"))

## Grid
title.grid(column=1,row=0)
canvas.grid(column=1,row=1)
start.grid(column=0,row=2)
reset.grid(column=2,row=2)
check.grid(column=1,row=3)




## Loop
window.mainloop()