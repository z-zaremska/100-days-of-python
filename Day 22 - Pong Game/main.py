from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_START_POSITIONS = [(350, 0), (-350, 0)]


# Game screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(800, 600)
screen.title('Pong')
screen.tracer(0)

# Create paddles for both players
paddle_R = Paddle(PADDLE_START_POSITIONS[0])
paddle_L = Paddle(PADDLE_START_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

# Paddles movement
screen.listen()
screen.onkeypress(paddle_R.move_up, 'Up')
screen.onkeypress(paddle_R.move_down, 'Down')
screen.onkeypress(paddle_L.move_up, 'w')
screen.onkeypress(paddle_L.move_down, 's')

ball_speed = 0.05

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision bal with paddle
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Paddle L wins
    if ball.xcor() > 400:
        ball.home()
        ball.bounce_x()
        scoreboard.add_point('L')

    # Paddle R wins
    if ball.xcor() < -400:
        ball.home()
        ball.bounce_x()
        scoreboard.add_point('R')


screen.exitonclick()
