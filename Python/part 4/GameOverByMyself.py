from turtle import Turtle
FONT = ("Alternate Gothic", 30, "bold")
FONT1 = ("Courier", 15, "italic")
FONT2 = ("Good Times", 20, "bold")
#FONT3 = ("Good Times",15,"bold")
#FONT4 = ("Good Times",25,"bold")
ALLIGN = "center"


class Gameover:
    def gameover1(self):
        g = Turtle()
        g.penup()
        g.color("white")
        g.goto(0, 220)
        g.write(f" Game Over", align=ALLIGN, font=FONT)
        g.hideturtle()

    def text(self):
        t = Turtle()
        t.penup()
        t.color("white")
        t.goto(0, -260)
        t.write(f"Click anywhere on screen to exit the game ",
                align=ALLIGN, font=FONT1)
        t.hideturtle()

    def nor(self):
        n = Turtle()
        n.penup()
        n.color("white")
        n.goto(0, -195)
        n.write(f"OR", align=ALLIGN, font=FONT2)
        n.hideturtle()

    def click(self):
        c = Turtle("square")
        c.penup()
        c.color("white")
        c.goto(0, -135)
        c.write(f"CLICKHERE", align=ALLIGN, font=FONT2)
        c.hideturtle()
