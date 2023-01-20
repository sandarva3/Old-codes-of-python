from tkinter import *
from turtle import left
root = Tk()
root.geometry("700x500")

f1 = Frame(root,borderwidth=4,relief=SUNKEN,bg="black")
f1.pack(pady=50,anchor=N)

def hello():
    print("Helllo")
def hi():
    print("hi")
def bye():
    print("bye")
def computer():
    print("computer")
b = Button(f1,text="Click1",padx=15,pady=10,command=hello,anchor=NW)
b.pack(side=LEFT)
b1 = Button(f1,text="Click2",padx=15,pady=10,command=hi,anchor=NW)
b1.pack(side=LEFT)
b2 = Button(f1,text="Click3",padx=15,pady=10,command=bye,anchor=NW)
b2.pack(side=LEFT)
b3 = Button(f1,text="Click4",padx=15,pady=10,command=computer,anchor=NW)
b3.pack(side=LEFT)


root.mainloop()
