from turtle import *
import random
t = Turtle()

colormode(255)


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r, g, b)
    return randomcolor

directions = [0, 90, 180, 270]
widths = 15
t.speed("fastest")
t.shape("circle")
while True:
    t.width(widths)
    t.color(randomcolor())
    t.forward(20)
    t.setheading(random.choice(directions))


s = Screen()
s.exitonslick()
