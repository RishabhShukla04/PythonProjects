from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.speed('fastest')
        self.Draw_food()

    def Draw_food(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280)
        self.goto(randomx, randomy)
