from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.move()

    def move(self):
        choice = random.randint(0,1)
        if choice == 0:
            random_h = random.randint(-280, 280)
            self.goto(350, random_h)
        else:
            random_h = random.randint(-280, 280)
            self.goto(-350, random_h)
