from tkinter import *
root = Tk()
root.geometry("500x700")

def click():
    print("he")

root.title("Calculato")
svalue = StringVar()
svalue.set("0")
sc = Entry(root, textvariable=svalue, font="Helvetica 20 bold")
sc.pack(ipady=5, pady=30)
f1 = Frame(root, bg="")
f1.pack()
b = Button(f1, text="1", font="lucida 25 bold")
b.pack(side=LEFT, padx=15)
b.bind("<Button-1>", click)
b = Button(f1, text="2", font="lucida 25 bold")
b.pack(side=LEFT, padx=15)
b.bind("<Button-1>", click)
b = Button(f1, text="3", font="lucida 25 bold")
b.pack(side=LEFT, padx=15)
b.bind("<Button-1>", click)


root.mainloop()
