from turtle import Turtle, Screen, Pen
import random
import time
from snake import Snake
from food import Food
from score import Score
#create the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("SNAKE")
screen.tracer(0)
#initialise all objects
snake = Snake()
food = Food()
score_txt = Turtle()
score = Score()

#map keybinds to functions
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

#main game loop
def main():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # snake.collisionWall()
        if snake.snake_head.xcor() > 290 or snake.snake_head.ycor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() < -290:
            score.game_over()
            game_is_on = False

        if snake.snake_head.distance(food) < 15:
            food.Draw_food()
            score.add_score()
            snake.grow_snake()

        for part in snake.snake_body:
            if part == snake.snake_head:
                pass
            else:
                if part.distance(snake.snake_head) < 10:
                    score.game_over()
                    game_is_on = False


main()

    # x = snake.snake_head.xcor
    # y = snake.snake_head.ycor
    # if x > 300 or y > 300:
    #     game_is_on = False
    #     print("GAME OVER")



















screen.exitonclick()
