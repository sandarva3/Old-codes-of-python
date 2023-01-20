from turtle import *
import random
t = Turtle()


colormode(255)
def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
t.pensize(2)
t.speed("fastest")
def spirograph(size):
 for _ in range(int(360 / size)): 
  t.color(randomcolor())
  t.circle(100)
  t.setheading(t.heading() + size)

spirograph(5)


s = Screen()
s.exitonclick()

