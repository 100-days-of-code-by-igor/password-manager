import csv
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# STATIC
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_list += [random.choice(NUMBERS) for _ in range(nr_letters)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    #set new password
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    if email and password and website:
        is_ok = messagebox.askyesno(title=website, message=f"Those are details entered: \nEmail: {email} "
                                                           f"\nPassword: {password}\n Is it ok to save?")

        if is_ok:
            with open('passwords.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter="|")
                writer.writerow([email, password, website])
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.delete(0, END)
    else:
        messagebox.showerror(title="Wrong Input", message="Fields cannot be null")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ADDRESS@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
