from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.setpos(position)
        self.shape('square')
        self.shapesize(1, 5)
        self.penup()
        self.color('white')

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(20)
