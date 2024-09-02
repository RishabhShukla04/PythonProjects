from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score, line

#create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)


#initialise the paddles with their positions
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
score = Score()
line = line()

screen.update()
#turn the animations back on for the movements
# accepting keybinds
screen.listen()
screen.onkeypress(paddle1.move_up, 'Up')
screen.onkeypress(paddle1.move_down, 'Down')
screen.onkeypress(paddle2.move_up, 'w')
screen.onkeypress(paddle2.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle1) < 50 and ball.xcor() > 340:
        ball.bouncePaddle()
    if ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bouncePaddle()
    if ball.xcor() > 380:
        ball.reset()
        score.add_scoreL()

    if ball.xcor() < -380:
        ball.reset()
        score.add_scoreR()
        # game_is_on = False


screen.exitonclick()