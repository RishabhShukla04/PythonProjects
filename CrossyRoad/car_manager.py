from random import random
from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list =[]
        self.diff = 0

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.penup()
            car.setheading(180)
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.randomy = random.randint(-250, 250)
            car.goto(300,car.randomy)
            self.car_list.append(car)
    def move_car(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + self.diff)

    def next_level(self):
        self.diff += MOVE_INCREMENT
