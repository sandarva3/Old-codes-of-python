from turtle import Turtle

STARTINGPOSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.createsnake()
        self.head = self.parts[0]

    def createsnake(self):
        for position in STARTINGPOSITION:
          self.addparts(position)

    def addparts(self, position):
            newpart = Turtle("square")
            newpart.color("white")
            newpart.penup()
            newpart.goto(position)
            self.parts.append(newpart)
            self.head = self.parts[0]
    
    def reset(self):
        self.parts.clear()
        self.createsnake()


    #add new part to the snake    
    def extend(self):
        self.addparts(self.parts[-1].position())



    def move(self):
        for seg in range(len(self.parts) - 1, 0, -1):
            newx = self.parts[seg - 1].xcor()
            newy = self.parts[seg - 1].ycor()
            self.parts[seg].goto(newx, newy)
        self.head.forward(MOVEDISTANCE)

    def up(self):
       if self.head.heading() != DOWN:
         self.head.setheading(UP)

    def down(self):
       if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
       if self.head.heading() != RIGHT :
         self.head.setheading(LEFT)

    def right(self):
       if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)
