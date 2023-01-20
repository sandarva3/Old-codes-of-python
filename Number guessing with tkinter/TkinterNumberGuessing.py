from tkinter import *

root = Tk()
root.title("Super Computer")
root.geometry("800x700")
# Title
Label(text="WELCOME TO THE MOST ADVANCED SUPERCOMPUTING SYSTEM IN WORLD.", padx=15, pady=20, border=5, relief=SUNKEN,
      font="Helvatica 15 bold", fg="white", bg="grey").grid(row=0, column=0, padx=0, pady=30)
Label(text="SuperIntelligent computer that finds the number you Guessed", padx=15, pady=20, border=5, relief=SUNKEN,
      font="Helvatica 15 bold", fg="white", bg="dark red").grid(row=1, column=0, padx=0, pady=30)

# Operation text
Label(text="Lets play a game... DO you want to ?").grid(row=2, column=0)
Label(text="Enter 'y' for yes and 'n' for no in the given box below").grid(
    row=3, column=0)


def box():
    if user_entry.get() == 'y':
        Label(text="Guess any integer number. Enter 'y' if you did").grid(
            row=4, column=0)
    if user_entry.get() == 'yy':
        Label(text="Now add 10 in the number you've guessed,enter 'y' again after you did").grid(
            row=5, column=0)
    if user_entry.get() == 'yyy':
        Label(text="Now,subtract 6 out of the number. Enter 'y' again after finishing").grid(
            row=6, column=0)
    if user_entry.get() == 'yyyy':
        Label(text="Now again, subtract the original number you guessed out of the number you have").grid(
            row=7, column=0)
    if user_entry.get() == 'yyyyy':
        Label(text="The number you have now is  4.", font="Helvetica 15 bold",
              bg="dark blue", fg="white", border=2, relief=RAISED).grid(row=8, column=0)


# Entry text
Entry_response1 = Label(text="Enter your response here :",
                        font="Courier 15 normal", padx=10, pady=20)
Entry_response1.grid(row=10, column=0, padx=20, pady=30)

# Entry box
user_entry = StringVar()
user_value = Entry(root, textvariable=user_entry,
                   width=30, border=2, relief=RAISED)
user_value.grid(row=11, column=0, padx=20, pady=20)

# Submit button
submit = Button(text="Submit", bg="grey", border=2, relief=SUNKEN,
                fg="white", padx=10, command=box).grid(row=12, column=0)


root.mainloop()
