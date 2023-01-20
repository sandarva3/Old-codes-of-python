from turtle import Screen, Turtle
from Turtle import Player
from cars import Cars
from scoreboard import Scoreboard, High_score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
carmanager = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move2, "Down")

Highscore = High_score()
Highscore.high_score()
#FONT3 = ("Courier",24,"normal")
#t = Turtle
# t.penup()
# t.hideturtle()
#t.write("HighScore =",font=FONT3)
# t.goto(350,250)

gameon = True
while gameon:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move()
# detect collision with car
    for car in carmanager.allcars:
        if car.distance(player) < 20:
            score.gameover()
            gameon = False
# detect succesful crossing
    if player.isatfinishline():
        player.gotostart()
        carmanager.levelup()
        score.increaselevel()
        Highscore.updatehigh()


screen.exitonclick()
