from turtle import Turtle, Screen, time


s = Screen()
s.setup(width=600, height=600)
s.title("Snake Game")
s.bgcolor("black")
startingposition = [(0, 0), (-20, 0), (-40, 0)]
parts = []
for position in startingposition:
    newpart = Turtle("square")
    newpart.penup()
    newpart.color("white")
    newpart.goto(position)
    parts.append(newpart)
    
s.exitonclick()
