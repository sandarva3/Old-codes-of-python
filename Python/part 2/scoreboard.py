from turtle import Turtle

FONT = ("Courier",24,"normal")
FONT2 = ("Courier",24,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-350,250)
        self.write(f"Level = {self.level}",align="left",font=FONT)
    def updatescoreboard(self):
        self.clear()
        self.write(f"Level = {self.level}",align="left",font=FONT)

    def increaselevel(self):
        self.level += 1
        self.updatescoreboard()
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAMEOVER",align="Center",font=FONT2)
class High_score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.highscore = 1
        self.penup()
        #self.write(f"Highscore = {self.highscore}",align="right",font=FONT)
        self.color("black")
        self.goto(350,250)
    def high_score(self):
        self.color("black")
        self.write(f"HighScore = {self.highscore}",align="right",font=FONT)
        self.goto(350,250)
    def updatehigh(self):
        self.highscore += 1
    
    


