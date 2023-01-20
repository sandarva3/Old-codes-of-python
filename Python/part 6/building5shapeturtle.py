from turtle import Turtle,Screen
import random

t = Turtle()
t.shape("turtle")

colors = ["cyan","spring green","orange red","medium slate blue","yellow"]

def shape(i): 
 a = 360/i
 for _ in range(i):
   t.forward(100)
   t.right(a)

for side in range(3,10):
    shape(side)
    t.color(random.choice(colors))



s =Screen()
s.exitonclick()
