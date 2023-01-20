from tkinter import *
a = Tk()
#width x height
a.geometry("600x400")
#width, height
a.maxsize(600,400)
a.minsize(200,100) 
a = Label(text = "Hello world")
a.place()
a.pack()
a.mainloop()
