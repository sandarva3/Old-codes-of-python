from turtle import Turtle, Screen
import random
raceon = False
s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title=" Make Your Bet ",
                  prompt="Which turtle will win the Race?")
bet = bet.strip()
bet = bet.lower()
print(bet)

colors = ["red", "green", "yellow", "blue"]
ypostions = [120, 40, -40, -120]
allturtle = []
for turtleindex in range(0,4):
    t= Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtleindex])
    t.goto(x=-250, y=ypostions[turtleindex])
    allturtle.append(t)

if bet :
    raceon = True 
while raceon:
    for turtle in allturtle:
        if turtle.xcor() > 230:
            raceon = False
            winningcolor = turtle.pencolor()
            if winningcolor == bet:
                print(f" You've won. {winningcolor} is the winner ")
            else:
                print(f"You lose, {bet} color turtle lose the race.{winningcolor.upper()} won")

        randomspeed = random.randint(1,10)
        turtle.forward(randomspeed)

 
 #s.exitonclick()
 