from turtle import Turtle, Screen, clear

t = Turtle()
s = Screen()

def moveforward():
    t.forward(10)
def moveback():
    t.back(10)
def moveright():
    t.right(20)
    #t.forward(10)
def moveleft():
    t.left(20)
    #t.forward(10)
def cleardrawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    


s.listen(s)
s.onkey(moveforward,"w" )
s.onkey(moveback , "s")
s.onkey(moveright, "d" )
s.onkey(moveleft , "a")
s.onkey(cleardrawing, "c")


s.exitonclick()
 