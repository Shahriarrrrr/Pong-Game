from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 35, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.score1, align="left", font=FONT)
        self.goto(100, 250)
        self.write(self.score2, align="left", font=FONT)

    def l_point(self):

        self.score1 += 1
        self.update_scoreboard()

    def r_point(self):
        self.score2 += 1
        self.update_scoreboard()
