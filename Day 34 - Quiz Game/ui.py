from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Creates Quiz Game interface."""

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        false_img = PhotoImage(file='./images/false.png')
        true_img = PhotoImage(file='./images/true.png')

        self.score_label = Label(text=f'Score: {self.quiz.score}/10', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg='white', width=300, height=250)
        self.canvas.config()
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.q_text = self.canvas.create_text(
            150, 125,
            text='question text',
            font=('Arial', 20, 'italic'),
            width=280
        )

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        nq_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=f'{nq_text}')
        self.score_label.config(text=f'Score: {self.quiz.score}/10')

    def continue_or_end_game(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.q_text, text=f'Your score is: {self.quiz.score}/10 correct answers.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def press_true(self):
        self.quiz.check_answer('True')
        self.continue_or_end_game()

    def press_false(self):
        self.quiz.check_answer('False')
        self.continue_or_end_game()
