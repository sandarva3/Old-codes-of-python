from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Tkinter menu")

def mymenu():
    print("You clicked on menu")

def setting():
    print("You clicked on setting ")

#
#menu = Menu()
#menu.add_command(label="Menu",command=mymenu)
#menu.add_command(label="Setting",command=setting)
#
#root.config(menu=menu)

menubar = Menu(root)
filemenubar = Menu(menubar, tearoff=0)

filemenubar.add_command(label="delete",command=mymenu)
#add lines between the cascade
filemenubar.add_separator()
filemenubar.add_command(label="Save",command=setting)
filemenubar.add_command(label="Save as",command=mymenu)
#
filemenubar.add_separator()
filemenubar.add_command(label="print",command=setting)

menubar.add_cascade(label="File",menu=filemenubar)
root.config(menu=menubar)

root.mainloop()
