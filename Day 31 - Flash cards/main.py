from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')

# Pictures
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text='French', fill='black', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='word', fill='black', font=('Arial', 60, 'bold'))


# Buttons
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=1, row=1)


window.mainloop()
