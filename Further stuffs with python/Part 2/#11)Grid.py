from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("This is the Graphical User Interface from Python-Tkinter")
a = Label(text="user")
b = Label(text="pass")
a.grid()
b.grid()


#Variable Classes in Tkinter
'''
Boolean Var, Double Var, Int var, String var
'''
uservalue = StringVar()
passvalue = StringVar()

def funtion():
    print(f" Your uservalue is :{uservalue.get()} ")
    print(f" Your password is {passvalue.get()} ")

userentry = Entry(root, textvariable= uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row =0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=funtion).grid()

root.mainloop()