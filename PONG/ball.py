from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.xmove = random.randint(-10, 10)
        self.ymove = random.randint(-10, 10)


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        # choice = random.randint(0,1)
        # if choice == 0:
        #     random_h = random.randint(-280, 280)
        #     self.goto(350, random_h)
        # else:
        #     random_h = random.randint(-280, 280)
        #     self.goto(-350, random_h)

    def bounce(self):
        self.ymove *= -1

    def bouncePaddle(self):
        self.xmove *= -1

    def reset(self):
        self.goto(0, 0)