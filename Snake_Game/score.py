from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=('Courier', 24, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.write(self.write(f"You Lose! Final score is: {self.score}", align='center', font=('Courier', 24, 'normal'))
)