from turtle import Screen
from pongmovement import Turt
from ball import Ball
from score import Scoreboard
import time
s = Screen()
s.bgcolor("black")
s.setup(width=700,height=600)
s.title("Pong")
s.tracer(0)

t1 = Turt((-300,0))
t2=Turt((300,0))
ball = Ball()
sc = Scoreboard()

s.listen()
s.onkey(t1.moveup,"w")
s.onkey(t1.movedown,"s")
s.onkey(t2.moveup,"Up")
s.onkey(t2.movedown,"Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.motion)
    s.update()
    ball.move()
    #collision with wall
    if ball.ycor() == 280 or ballw.ycor() == -280:
        ball.bouncey()
        #collision with paddle
    if ball.distance(t2) < 50 and ball.xcor() > 280 or ball.distance(t1) < 50 and ball.xcor() < -280 :
      ball.bouncex()
    #right paddle misses
    if ball.xcor() > 320 :
      ball.reset_position()
      sc.lpoint()
    #left paddle misses
    if ball.xcor() < -320:
      ball.reset_position()
      sc.rpoint()
    


s.exitonclick()