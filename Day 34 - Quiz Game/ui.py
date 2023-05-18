from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    """Creates Quiz Game interface."""

    def __init__(self):
        self.score = 0
        self.current_question = 'Question'

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.false_img = PhotoImage(file='./images/false.png')
        self.true_img = PhotoImage(file='./images/true.png')

        self.score_label = Label(text=f'Score: {self.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg='white', width=300, height=250, highlightthickness=20, highlightbackground=THEME_COLOR)
        self.canvas.config()
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.canvas.create_text(175, 150, text=self.current_question, font=('Arial', 20, 'italic'))

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
