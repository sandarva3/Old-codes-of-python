from tkinter import *
root = Tk()
root.geometry("800x600")

f1 = Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l = Label(f1,text = "Tkinter GUI")
l.pack(pady=150,padx=50)

f2 = Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l2 = Label(f2,text = "This is the GUI from Tkinter Python")
l2.pack(pady=50,padx=50)

f3 = Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f3.pack(side=TOP,fill=X)
l2 = Label(f3,text = "Is this GUI good ?")
l2.pack(pady=50,padx=50)



root.mainloop()
