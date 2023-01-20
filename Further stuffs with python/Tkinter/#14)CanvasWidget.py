from contextlib import redirect_stderr
from sys import builtin_module_names
from tkinter import *
from unittest import TestCase
root = Tk()
canvas_width = 800
canvas_height = 600
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#The line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,600,fill="red")
can_widget.create_line(0,600,800,0,fill="red")

#To create rectangle define the coordinates of top left and bottom right
can_widget.create_rectangle(10,80,200,200, fill="blue")

#To create text, specify x and y coordinates.
can_widget.create_text(70,65,text="This is oval inside rectangle")

#To create oval give the coordinates of top left and bottom right
can_widget.create_oval(10,80,200,200,fill="black")

root.mainloop()
