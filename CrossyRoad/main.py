import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#
player = Player()
cars = CarManager()
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    for car in cars.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 250:
        player.reset()
        cars.next_level()
        scoreboard.next_level()






screen.exitonclick()
