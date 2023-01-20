from turtle import Turtle, Screen
import random
import turtle

s = Screen()

s.setup(width=500, height=400)
bet = s.textinput(title=" Make Your Bet ",
                  prompt="Which turtle will win the Race?")
print(bet)

colors = ["red", "green", "yellow", "blue"]
ypostions = [120, 40, -40, -120]

for turtleindex in range(0,4):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtleindex])
    t.goto(x=-250, y=ypostions[turtleindex])

s.exitonclick()
