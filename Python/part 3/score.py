from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.rscore = 0
        self.lscore = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 220)
        self.write(f"Score: {self.lscore}", align=ALLIGNMENT, font=FONT)
        self.goto(150, 220)
        self.write(f"Score: {self.rscore}", align=ALLIGNMENT, font=FONT)

    def lpoint(self):
        self.lscore += 1
        self.update_scoreboard()
    def rpoint(self):
        self.rscore += 1
        self.update_scoreboard()

   