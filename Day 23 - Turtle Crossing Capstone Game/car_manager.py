from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle('square')
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
