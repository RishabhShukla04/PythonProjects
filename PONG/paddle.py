from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.width(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


#old method used before realising 1 class was more efficient
# class Paddle1(Paddle):
#     def __init__(self):
#         super().__init__()
#         self.paddle.goto(350, 0)
#
#
# class Paddle2(Paddle):
#     def __init__(self):
#         super().__init__()
#         self.paddle.goto(-350, 0)
