from turtle import Screen
from snake1 import Snake
from FoodForSnake import Food
from scoreboard1 import Scoreboard
import time
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()


s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
scoreboard = Scoreboard()


game = True
while game:
    s.update()
    time.sleep(0.1)

    snake.move()
 # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()

 # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       scoreboard.reset()
       snake.reset()
           # scoreboard.gameover()

    for parts in snake.parts:
        if parts == snake.head:
            pass
        elif snake.head.distance(parts) < 10:
            scoreboard.reset()
            snake.reset()
            
            #scoreboard.gameover()


s.exitonclick()
