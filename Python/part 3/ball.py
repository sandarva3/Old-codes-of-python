from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.motion = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
    
    def bouncey(self):
        self.ymove *= -1
    
    def bouncex(self):
        self.xmove *= -1
        self.motion *= 0.9
    
    def reset_position(self):
        self.motion = 0.1
        self.goto(0,0)
        self.bouncex()

    
