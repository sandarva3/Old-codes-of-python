from turtle import Turtle

class Turt(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def movedown(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)

    def moveup(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)
