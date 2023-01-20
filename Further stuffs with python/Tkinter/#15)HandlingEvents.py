from ast import Return
from tkinter import *
from turtle import width
root = Tk()
root.title(" Tkinter practice ")
root.geometry("800x600")
def hello(event):
    print(f"you clicked the button at {event.x},{event.y} ")
widget = Button(root, text="Click here")
widget.pack() 
widget.bind('<Button-1>',hello)
widget.bind("<Double-1>", quit)



root.mainloop()
