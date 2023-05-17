from card import CardManager
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WORDS = pd.read_csv('./data/french_words.csv')
WORDS = WORDS.to_dict(orient='records')

card_manager = CardManager('french', 'english')
card_manager.create_cards(WORDS)


# --------------------------- Update card layout ------------------------------ #
def update_card_layout(lang, word, picture):
    canvas.itemconfig(language_text, text=lang)
    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(card_layout, image=picture)


# --------------------------- Display next card ------------------------------ #
def next_card():
    global current_card
    current_card = random.choice(card_manager.unguessed_cards)
    update_card_layout(current_card.language_A, current_card.word_A, card_front_img)


# --------------------------- Card guessed -------------------------------- #
def card_not_guessed():
    global current_card
    update_card_layout(current_card.language_B, current_card.word_B, card_back_img)
    window.after(3000, next_card)


# --------------------------- Card guessed ------------------------------ #
def card_guessed():
    global current_card
    card_manager.add_card_to_guessed(current_card)
    next_card()


# --------------------------- GUI ------------------------------ #
# Window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')

# Pictures
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

# Canvas (card)
current_card = random.choice(card_manager.unguessed_cards)
current_language = current_card.language_A
current_word = current_card.word_A

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_layout = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text=current_language.title(), fill='black', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text=current_word.lower(), fill='black', font=('Arial', 60, 'bold'))

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=card_guessed)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_not_guessed)
wrong_button.grid(column=1, row=1)


window.mainloop()
