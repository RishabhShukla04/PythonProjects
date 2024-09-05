from turtle import Turtle, Screen
import pandas
screen = Screen()
background = Turtle()
screen.addshape("./blank_states_img.gif")
background.shape("./blank_states_img.gif")




states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()


def states_guess():
    answer = str(screen.textinput("Guess a state", "What's your guess?")).title()
    if answer in states_list:
        t = Turtle()
        t.hideturtle()
        t.penup()
        x_cor = states[states.state == answer].x
        y_cor = states[states.state == answer].y
        t.goto(int(x_cor), int(y_cor))
        t.write(f"{answer}", align='center', font=('Courier', 16, 'normal'))
        states_list.remove(answer)
        if len(states_list) == 0:
            t.clear()
            t.goto(0,0)
            t.write(f"{"GAME OVER"}", align='center', font=('Courier', 34, 'normal'))
    if answer == "Exit":
        exit(0)

game_is_on = True
while game_is_on:
    states_guess()
screen.mainloop()






