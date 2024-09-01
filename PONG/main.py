from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

#create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)


#initialise the paddles with their positions
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
screen.tracer(1)
ball = Ball()

screen.update()
#turn the animations back on for the movements
# accepting keybinds
screen.listen()
screen.onkeypress(paddle1.move_up, 'Up')
screen.onkeypress(paddle1.move_down, 'Down')
screen.onkeypress(paddle2.move_up, 'w')
screen.onkeypress(paddle2.move_down, 's')


screen.exitonclick()

game_is_on = True
while game_is_on:
    ball.move()

