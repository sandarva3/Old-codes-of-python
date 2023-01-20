from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("This is the GUI from TKinter")
#Important Lable Options
'''
# bd = background
# fg = foreground
# one way )font : font = "Courier 19 bold"
another way) : font=("Courier",9,"bold")
padx = x _Padding
pady = y _Padding
relief = border styling = SUNKEN, RAISED, GROOVE,RIDGE
 '''
title_label = Label(text = ''' One of the most important skills of an AI architect is the ability to
\n identify ideas that are worth working on. Over the years, 
\n I’ve had fun applying machine learning to manufacturing, healthcare, 
\n climate change, agriculture, ecommerce, advertising, and other industries.
\n How can someone who’s not an expert in all these sectors find meaningful projects within them?
\n Here are five steps to help you scope projects effectively.''', bg = "red", fg="white",
padx=30, pady=40,font=("Courier",9,"bold"), borderwidth=3, relief=SUNKEN)

#Important pack options
'''
anchor =nw,sw,e,w,ne ......
side = top, bottom, left, right
fill = x(fill the horizantal part), y(fill the vertical part) 
padx
pady
'''
title_label.pack(side= RIGHT,anchor=SW, fill=Y)

root.mainloop()