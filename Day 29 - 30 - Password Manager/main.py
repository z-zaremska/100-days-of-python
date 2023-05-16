from tkinter import *
from tkinter import messagebox
import json
import os
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    new_password = ''
    for i in range(10):
        letter = random.choice(string.ascii_letters)
        number = str(random.randint(0, 10))
        new_password += random.choice([letter, number])

    password_entry.insert(0, f'{new_password}')


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def load_passwords():
    if os.path.exists('my_passwords.json'):
        with open('my_passwords.json', 'r') as f:
            return json.load(f)
    else:
        return {}


# ---------------------------- SEARCH FOR PASSWORD ------------------------------- #
def search_for_website():
    searched_website = search_entry.get().lower()
    password_entry.delete(0, END)
    website_entry.delete(0, END)
    username_entry.delete(0, END)

    try:
        searched_username = PASSWORDS[f'{searched_website}']['username']
        searched_password = PASSWORDS[f'{searched_website}']['password']

        website_entry.insert(0, searched_website)
        username_entry.insert(0, searched_username)
        password_entry.insert(0, searched_password)

    except KeyError:
        messagebox.showinfo(title='Website not found', message=f'Sorry, but website {searched_website.title()} was '
                                                               f'not found')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_for_website():
    searched_website = search_entry.get().lower()
    password_entry.delete(0, END)
    website_entry.delete(0, END)
    username_entry.delete(0, END)

    try:
        searched_username = PASSWORDS[f'{searched_website}']['username']
        searched_password = PASSWORDS[f'{searched_website}']['password']

        website_entry.insert(0, searched_website)
        username_entry.insert(0, searched_username)
        password_entry.insert(0, searched_password)

    except KeyError:
        messagebox.showinfo(title='Website not found', message=f'Sorry, but website {searched_website.title()} was '
                                                               f'not found')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) < 3 or len(username) < 3 or len(password) < 8:
        messagebox.showinfo(title='No valid data', message='All fields must be fulfilled!')
    else:
        # Pop-up message about successful operation
        is_ok = messagebox.askokcancel(title=website, message=f'Your username: {username}\nYour password: {password}\n'
                                                              f'\nDo you want to save it?')

        if is_ok:
            PASSWORDS[f'{website}'] = {}
            PASSWORDS[f'{website}']['username'] = username
            PASSWORDS[f'{website}']['password'] = password

            with open('my_passwords.json', 'w') as f:
                json_passwords = json.dumps(PASSWORDS, indent=3)
                f.write(json_passwords)

            password_entry.delete(0, END)
            website_entry.delete(0, END)
            search_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
PASSWORDS = load_passwords()

window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=2)

username_label = Label(text='E-mail\\Username:')
username_label.grid(column=0, row=3)

password_label = Label(text='Password:')
password_label.grid(column=0, row=4)

# Entries
search_entry = Entry(width=35)
search_entry.grid(column=1, row=1)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=2, columnspan=2)
# set cursor in website entry field
website_entry.focus()
website_entry.insert(END, '')

username_entry = Entry(width=53)
username_entry.grid(column=1, row=3, columnspan=2)
username_entry.insert(END, 'your_fav_email@gmail.com')

password_entry = Entry(width=35)
password_entry.grid(column=1, row=4)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=4)

add_button = Button(text='Add', width=45, command=add_password)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text='Search', width=13, command=search_for_website)
search_button.grid(column=2, row=1)

window.mainloop()
