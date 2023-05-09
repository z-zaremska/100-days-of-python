from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', align='center', font=FONT)
