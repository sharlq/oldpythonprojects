import tkinter
from tkinter import * # its important if it says Tk is not defined
from functools import partial # its needed for the ability to access the function
win =Tk()

frame = Frame(win)# declaring a frame
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame,text='Red',fg='red')
rb.pack(side=LEFT)
rb2 = Button(frame2,text='green',fg='green')
rb2.pack(side=BOTTOM)

win.mainloop()