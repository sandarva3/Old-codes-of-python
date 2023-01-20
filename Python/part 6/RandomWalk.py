from turtle import Turtle, Screen, color, window_width
import random

t = Turtle()
colors = ["blue", "deep pink", "blue violet", "medium spring green", "lime",
          "cyan", "spring green", "orange red", "medium slate blue", "yellow"]
shapes = ["turtle", "classic", "arrow", "circle", "square", "triangle"]
directions = [0,90,180,270]
#write = ["Hello", "Hi"]
#widths = 15
t.speed("fastest")
t.pensize(15)
while True:
   # t.width(widths)
    t.forward(20)
    t.setheading(random.choice(directions))
    t.color(random.choice(colors))
    t.shape(random.choice(shapes))
 

    #t.write(write)
    
    



s = Screen()
s.exitonclick()
