from tkinter import *
from tkinter import messagebox
import pandas
from random import choice,randint,shuffle
import pyperclip
import json

OUTFILE = "01-Programming-Language\\01-Python\\01-100-Days-of-Code\\29,30-Password-Manager\\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0,END)
    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website = entry_web.get()
    username = entry_user.get()
    password = entry_password.get()

    new_data ={
        website: {
            "username":username,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",message=f"These are the details entered: \nUsername: {username}\nPassword: {password}\n\nSave?")
        if is_ok:
            try:
                with open(OUTFILE,"r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(OUTFILE,"w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open(OUTFILE,"w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_web.delete(0,END)
                entry_password.delete(0,END)

# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    website = entry_web.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please enter a website!")
    else:
        try:
            with open(OUTFILE,"r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error",message="There are no saved passwords.")
        else:
            try:
                username = data[website]['username']
                password = data[website]['password']
            except KeyError:
                messagebox.showerror(title="Error",message=f"No saved passwords for {website}")
            else:
                messagebox.showinfo(title=f"{website} Password",message=f"Username: {username}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
## Window
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

## Logo
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo = PhotoImage(file="01-Programming-Language\\01-Python\\01-100-Days-of-Code\\29,30-Password-Manager\\logo.png")
canvas.create_image(100,100,image=logo)


## Labels
label_web = Label(text="Website: ",pady=5)
label_user = Label(text="Email/Username: ",pady=5)
label_password = Label(text="Password: ",pady=5)

## Entries
entry_web = Entry(width=31)
entry_web.focus()
entry_user = Entry(width=51)
entry_user.insert(END, "testingemail@gmail.com")
entry_password = Entry(width=31)


## Buttons
button_genpass = Button(text="Generate Password",command=gen_password)
button_add = Button(text="Add",width=43,command=save_password)
button_search = Button(text="Search",width=15,command=find_password)

## Grid
canvas.grid(column=1,row=0)
label_web.grid(column=0,row=1,sticky="W")
entry_web.grid(column=1,row=1,sticky="W")
button_search.grid(column=2,row=1,sticky="W")
label_user.grid(column=0,row=2,sticky="W")
entry_user.grid(column=1,row=2,columnspan=2,sticky="W")
label_password.grid(column=0,row=3,sticky="W")
entry_password.grid(column=1,row=3,sticky="W")
button_genpass.grid(column=2,row=3,sticky="W")
button_add.grid(column=1,row=4,columnspan=2,sticky="W")


window.mainloop()
