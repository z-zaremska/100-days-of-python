from turtle import Turtle

CENTER = 'center'
FONT = ('Calibri Light', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_R = 0
        self.score_L = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 250)
        self.write('Score:', align=CENTER, font=FONT)
        self.goto(-100, 200)
        self.write(self.score_L, align='left', font=FONT)
        self.goto(100, 200)
        self.write(self.score_R, align='right', font=FONT)

    def add_point(self, player):
        if player == 'R':
            self.score_R += 1
        else:
            self.score_L += 1

        self.clear()
        self.update_scoreboard()
