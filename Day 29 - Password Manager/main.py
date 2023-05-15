from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text='E-mail\\Username:')
username_label.grid(column=0, row=2)
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3)
generate_password_button = Button(text='Generate Password')
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add')
add_button.grid(column=1, row=4)

window.mainloop()
