from email.mime import image
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
#root.geometry("1000x800")

image1 = Image.open("1.jpeg")
resizedimage1 = image1.resize((400,350), Image.ANTIALIAS)
image11 = ImageTk.PhotoImage(resizedimage1)
text1 = open("1t.txt", "r")
f1 = Frame(image1)

image2 = Image.open("2.jpg")
resizedimage2 = image2.resize((400,350), Image.ANTIALIAS)
image22 = ImageTk.PhotoImage(resizedimage2)
text2 = open("2t.txt", "r")

image3 = Image.open("3.jpeg")
resizedimage3 = image3.resize((400,350), Image.ANTIALIAS)
image33 = ImageTk.PhotoImage(resizedimage3)
text3 = open("3t.txt", "r") 

image11 = Frame(root)

image111 = Label(image=image11)
text11 = Label(text=text1)
image222 = Label(image=image22)
text22 = Label(text=text2)
image333 = Label(image=image33)
text33 = Label(text=text3)
#text33.grid(row=5,column=0)


image111.pack( side= TOP , anchor=NW)
text11.pack( side= TOP , anchor=W)
image222.pack( side= TOP , anchor=NE)
text22.pack( side= TOP , anchor=W)
image333.pack( side= TOP , anchor=W)
text33.pack( side= TOP , anchor=W)


root.mainloop()
