from tkinter import *
import json
import os

passwords = {}

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def load_passwords():
    if os.path.exists('my_passwords.json'):
        with open('my_passwords.json', 'r') as f:
            global passwords
            passwords = json.load(f)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    passwords[f'{website}'] = {}
    passwords[f'{website}']['username'] = username
    passwords[f'{website}']['password'] = password

    with open('my_passwords.json', 'w') as f:
        json_passwords = json.dumps(passwords, indent=3)
        f.write(json_passwords)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

load_passwords()

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='E-mail\\Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
# set cursor in website entry field
website_entry.focus()
website_entry.insert(0, 'https://')

username_entry = Entry(width=53)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, '@gmail.com')

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=45, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
