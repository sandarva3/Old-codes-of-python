from tkinter import *
#To import other kinds of image except PNG (particularly JPG,JPEG)
from PIL import Image, ImageTk
a = Tk()
#a.geometry("1600x1500")
a.title("Tkinter Python")
c = Image.open("CodeWithHarry\Tkinter\CopaAmerica.jpg")
d = ImageTk.PhotoImage(c)

photo = PhotoImage(file="CodeWithHarry\Tkinter\pasport.png")
b = Label(image=d)
f = Label(image=photo)
b.pack() # b is at the first so the image of copa america will be shown first
f.pack()


a.mainloop()