from turtle import Turtle

LOAD_POSITION = [(0,0), (-20,0), (-40,0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.Draw_snake()
        self.snake_head = self.snake_body[0]

    def Draw_snake(self):
        for i in LOAD_POSITION:
            self.add_part(i)

    def move(self):
        for num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[num - 1].xcor()
            new_y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    # def collisionWall(self):
    #     if self.snake_head.xcor > 280 or self.snake_head.ycor > 280 or self.snake_head.xcor() < -280 or self.snake_head.ycor() < -280:
    #         print("Collision Wall")

    # def collisionTail(self):
    #     for segments

    def add_part(self, position):
        snakepart = Turtle()
        snakepart.color("white")
        snakepart.shape("square")
        snakepart.penup()
        snakepart.goto(position)
        self.snake_body.append(snakepart)
    def grow_snake(self):
        self.add_part(self.snake_body[-1].position())

