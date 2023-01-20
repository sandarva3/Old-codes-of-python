from turtle import Turtle, Screen, xcor
import random

startrace = False
s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Snake game ",
                  prompt="Which turtle do you think will win the race ?")

ycordinates = [150, 80, 10, -60, -130]
colors = ["yellow", "green", "blue", "red", "black"]
allturtle = []

for turtleindex in range(0, 5):
    t = Turtle("turtle")
    t.penup()
    t.goto(-230, ycordinates[turtleindex])
    t.color(colors[turtleindex])
    allturtle.append(t)

if bet:
    startrace = True

while startrace:
    for turtle in allturtle:
        randomspeed = random.randint(1, 10)
        turtle.forward(randomspeed)
        if (turtle).xcor() > 220:
            startrace = False
            winturtle = turtle.pencolor()
            if bet == winturtle:
                print(f"Congrats ! You won bet. {bet} turtle won the race. ")
            else:
                print(
                    f"You lose bet. {bet} turtle lose the race, {winturtle.upper()} won the race.")


s.exitonclick()
