from tkinter import *
root = Tk()
root.title("Super Intelligent computer that finds the Number you guess")
root.geometry("800x700")

#Frame in top of the screen
f1 = Frame(root, bg="black", border=5, relief=SUNKEN)
f1.grid(pady=40,row=0,column=0)
l1 = Label(f1, text="Welcome To SuperIntelligent System",font="Buffalo 25 bold", bg="grey", fg="white",padx=4,pady=7)
l1.grid(padx=10,pady=12)


Label(text="lets play a game").grid(pady=20,row=1,column=0)
c = Label(text="Enter 'y' if you want to and 'n' if you don't : ").grid(row=2,column=0)

def getuser():
        if (user_entry.get()) == 'y':

            Label(text="Guess any number between 1 to 10").grid(row=2,column=0)
        #if user_entry.get() == 'y':
        #          Label(text="Have you guessed, Enter 'y' after guessing :").grid(row=2,column=0)
    
#Text for user entry box
Label(root, text= "Enter your response here :",font="Courier 15 normal").grid(pady=70,row=3,column=0)

#box for user input
user_entry = StringVar()
entry_box = Entry(root, textvariable=user_entry)
entry_box.grid(pady=20,row=4,column=0)

#Button for user response
user_response = Button(text="Enter",padx=25,pady=5,border=3,relief=RAISED,command=getuser)
user_response.grid(row=5,column=0)




root.mainloop()
