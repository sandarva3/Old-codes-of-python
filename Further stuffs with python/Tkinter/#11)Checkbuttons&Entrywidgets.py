from cgi import test
from re import sub
from tkinter import *
root = Tk()
root.geometry("800x700")
#Heading of our forom
Label(root,text="This is the program",font="Helvetica 15 bold",pady=20,padx=30,border=3,relief=GROOVE).grid(row=0,column=3,pady=15)

#Text names for the form
name =Label(root,text="Name")
phone = Label(root,text="Phone")
address = Label(root,text="Address")
gender = Label(root,text="Gender")
age = Label(root,text="Age")

#Text names position for the form
name.grid(row=1,column=2,padx=10)
phone.grid(row=2,column=2,padx=10)
address.grid(row=3,column=2,padx=10)
gender.grid(row=4,column=2,padx=10)
age.grid(row=5,column=2,padx=10)

#User input data types value for the form
namevalue = StringVar()
phonevalue = StringVar()
addvalue = StringVar()
genvalue = StringVar()
agevalue = StringVar()
foodvalue = IntVar()

#User input 
nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
addentry = Entry(root,textvariable=addvalue)
genentry = Entry(root,textvariable=genvalue)
ageentry = Entry(root,textvariable=agevalue)   

#User input position
nameentry.grid(row=1,column=3,padx=0,pady=5)
phoneentry.grid(row=2,column=3,padx=0,pady=5)
addentry.grid(row=3,column=3,padx=0,pady=5)
genentry.grid(row=4,column=3,padx=0,pady=5)
ageentry.grid(row=5,column=3,padx=0,pady=5)

#Checkbutton
food = Checkbutton(text="Check here if you want your meals at lower cost ",variable=foodvalue)
food.grid(row=6,column=3,pady=10)

#Command for the button below
def submit():
    Label(text="Thank You",font="Buffalo 20 bold").grid(row=10,column=5)

def submit1():
    Label(text="Does it worked ?",font="Buffalo 20 bold").grid(row=10,column=5)
#Button and assigning at a command
button = Button(text="Submit",command=submit)
button.grid(row=7,column=3)




root.mainloop()