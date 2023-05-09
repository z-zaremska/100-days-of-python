from turtle import Turtle
import datetime as 


ALIGMENT = 'center'
FONT = ('Calibri Light', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.retrieve_score()
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | Highest score: {self.highest_score}', align=ALIGMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score

        self.score = 0
        self.update_scoreboard()

    def save_score(self):
        text_to_save = f"Highest score: {self.highest_score}\nDate: {dt.datetime.now()}"

        with open('snake_top_score.txt', 'w') as file:
            file.write(text_to_save)

    def retrieve_score(self):
        try:
            with open('snake_top_score.txt', 'r') as file:
                first_line = file.readline().strip('\n')
                self.highest_score = int(first_line[15:])
        except FileNotFoundError:
            pass
