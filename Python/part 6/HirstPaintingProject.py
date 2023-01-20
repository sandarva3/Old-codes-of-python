'''THiS IS WRONG 
 import colorgram
rgbcolors = []
colors = colorgram.extract("FromMega/Day18/Hirstimage.jpg",30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new = (r, g, b)
    rgbcolors.append(new)
print(rgbcolors) '''

from turtle import *
Screen
import random
colormode(255)
maincolor = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
t = Turtle()
t.speed("fastest")
t.hideturtle()
#t.shape("arrow")
t.penup()
t.setheading(220)
t.forward(370)
t.setheading(0)
for dot_count in range(1, 101):
 t.dot("20",random.choice(maincolor))
 t.forward(50)

 if dot_count % 10 ==0:
  t.setheading(90)
  t.forward(50)
  t.setheading(180)
  t.forward(500)
  t.setheading(0)





s = Screen()
s.exitonclick()


