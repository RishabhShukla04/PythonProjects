from turtle import Turtle as T, Screen, colormode
import random

tom = T()
tom.shape('turtle')
tom.color('plum4')

# def draw_shape(numberofsides):
#     angle = 360 / int(numberofsides)
#     for i in range(numberofsides):
#         tom.forward(100)
#         tom.left(angle)
#
# draw_shape(3)
#
# for num in range (3,10):
#     draw_shape(num)
#

directions = [0, 90, 180, 270]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

colormode(255)

tom.speed("fastest")
for num in range(1000):
    tom.color(random_colour())
    dir = random.choice(directions)
    tom.setheading(dir)
    tom.forward(10)

#


screen = Screen()
screen.exitonclick()