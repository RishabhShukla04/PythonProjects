from turtle import Turtle

LOAD_POSITION = [(0,0), (-20,0), (-40,0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.Draw_snake()

    def Draw_snake(self):
        for i in LOAD_POSITION:
            snakepart = Turtle()
            snakepart.color("white")
            snakepart.shape("square")
            snakepart.penup()
            snakepart.goto(i)
            self.snake_body.append(snakepart)

    def move(self):
        for num in range(2, 0, -1):
            new_x = self.snake_body[num - 1].xcor()
            new_y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

