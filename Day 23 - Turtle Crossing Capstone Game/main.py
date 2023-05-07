import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, 'Up')

counter = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.move_forward()
    counter += 1

    # Detect player crossing the line
    if player.ycor() > 280:
        scoreboard.next_level()
        player.new_game()
        car_manager.speed_up()

    # Detect collision between player and car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

scoreboard.game_over()
screen.exitonclick()
