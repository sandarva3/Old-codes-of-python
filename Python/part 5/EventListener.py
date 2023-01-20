from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def moveforward():
    t.forward(10)


s.listen(s)
s.onkey( key = "space", fun = moveforward )
s.exitonclick()
