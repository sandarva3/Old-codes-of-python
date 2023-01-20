from string import whitespace
from turtle import Turtle , Screen, xcor
import turtle
s = Screen()
s.bgcolor("black")
s.setup(width=500, height=400)
s.title("My own Snake Game")

t = Turtle("square")
t2 = Turtle("square")
t3 = Turtle("square")

t.penup()
t2.penup()
t3.penup()

t.color("white")
t.goto(-20,0)

t2.color("white")

t3.color("white")
t3.goto(20,0)

s.listen(s)
def moveforward():
 for _ in range(50):
    t.forward(10)
    t2.forward(10)
    t3.forward(10)


    
def moveleft():
    t.left(90)
    for _ in range(50):
        t.forward(10)
        t2.left(90)
        t2.goto(xcor(+20),0)
        t2.forward(10)
        t3.left(90)
        t3.goto(xcor(+40),0)
        t3.forward(10)
        
#
#   
#def moveleft(): 
s.onkey(moveforward, "w")
s.onkey(moveleft,"a")




s.exitonclick()