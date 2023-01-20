from calendar import c
from tkinter import *
root = Tk()
width = input("Enter how much widthe do you want ?")
height = input("Enter how much height do you want ?")
root.geometry(f"{width}x{height}")
def hello(event):
    print(f"you clicked the button at {event.x},{event.y} ")
root.title("This the window according to your size")
Label(text="TO close this window you can click in the button below").grid(row=0,column=0)






root.mainloop()