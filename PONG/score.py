from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        # self.goto(-200, 250)
        self.left_score = 0
        self.right_score = 0
        self.update_score()
        # self.goto(200, 250)
        # self.update_Rscore()

    # def update_Lscore(self):
    #     self.write(f"{self.left_score}", align='center', font=('Courier', 24, 'normal'))
    # def update_Rscore(self):
    #     self.write(f"{self.right_score}", align='center', font=('Courier', 24, 'normal'))


    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"{self.left_score}", align='center', font=('Courier', 24, 'normal'))
        self.goto(200, 250)
        self.write(f"{self.right_score}", align='center', font=('Courier', 24, 'normal'))

    def add_scoreL(self):
        self.left_score += 1
        self.update_score()

    def add_scoreR(self):
        self.right_score += 1
        self.update_score()


class line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)

