from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write(f"Score: {self.score} HighScore : {self .highscore}" , align = ALLIGNMENT , font = FONT )
        self.hideturtle()
    
    def updatescoreboard(self):
            self.clear() 
            self.write(f"Score: {self.score}" , align = ALLIGNMENT, font = FONT )
    
    def reset(self):
        for seg in self.parts:
            seg.goto(1000,1000)
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.updatescoreboard()



    #def gameover(self):
    #    self.goto(0,0)
    #    self.write(f"Game Over" , align = ALLIGNMENT, font = FONT )

    def increasescore(self):
            self.score += 1 
            self.updatescoreboard()
