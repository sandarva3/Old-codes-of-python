from turtle import Turtle
import random
Colors = ["red", "yellow", "blue", "green",
    "black", "orange", "pink", "purple"]
startingmovedistance = 5
moveincrement = 10
     


class Cars():
        def __init__(self):
            super().__init__()
            self.allcars = []
            self.carspeed = startingmovedistance
 
        def create_cars(self):
          randomchance = random.randint(1,6)
          if randomchance == 1:
              newcar = Turtle("square")
              newcar.shapesize(stretch_wid=1, stretch_len=2)
              newcar.penup()
              newcar.color(random.choice(Colors))
              randomy = random.randint(-250, 250)
              newcar.goto(400, randomy)
              self.allcars.append(newcar)
        
        def move(self):
          for car in self.allcars:
            car.backward(self.carspeed)
        
        def levelup(self):
          self.carspeed += 5



      
   