from turtle import Turtle
starting_position = (0,-280)
finishline = 300
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(starting_position)
    
    def move(self):
        self.forward(10)
    def move2(self):
        self.backward(10)
    
    def gotostart(self):
        self.goto(starting_position)

    def isatfinishline(self):
        if self.ycor() > finishline:
            return True
        else:
            return False




