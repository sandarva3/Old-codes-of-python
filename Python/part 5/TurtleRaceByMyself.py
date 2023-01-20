from turtle import Turtle, Screen
import random

t1 = Turtle()
t1.color("green")
t1.shape("turtle")
t1.penup()

t2 = Turtle()
t2.color("blue")
t2.shape("turtle")
t2.penup()

t3 = Turtle()
t3.color("red")
t3.shape("turtle")
t3.penup()

t4 = Turtle()
t4.color("black")
t4.shape("turtle")
t4.penup()
s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title=" Make Your Bet ",
                  prompt="Which turtle will win the Race?")
print(bet)

def function():
    t1.goto(x=-225, y=120)
    t2.goto(x=-225, y=40)
    t3.goto(x=-225, y=-20)
    t4.goto(x=-225, y=-100)

function()

for _ in range(80):
    #forwards = random.randint(1,10)
    t1.forward(random.randint(1,10))
    t2.forward(random.randint(1,10))
    t3.forward(random.randint(1,10))
    t4.forward(random.randint(1,10))
if (t1.xcor > 230):
    print(f"{t1.color()} won the race")
elif (t2.xcor > 230):
    print(f"{t2.color()} won the race")
elif (t3.xcor > 230):
    print(f"{t3.color()} won the race")
elif (t4.xcor > 230):
    print(f"{t4.color()} won the race")
else:
    print("none")


s.exitonclick() 