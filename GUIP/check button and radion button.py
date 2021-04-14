import tkinter
from tkinter import * # its important if it says Tk is not defined

win =Tk()
var=IntVar()
c1 = IntVar() # we need variable to safe the value of the button and we declare it this way
ch = Checkbutton(win, text= "musicl", offvalue = 0, onvalue=1 , height=5, width=10 , variable=c1)



r= Radiobutton(win, text = "option 1" ,variable = var, value = 1) # it has one value and just one var can be checked in

r2= Radiobutton(win, text = "option 2" ,variable = var, value = 2) # it has one value
r3= Radiobutton(win, text = "option 3" ,variable = var, value = 3) # it has one value
ch.pack()
r.pack()
r2.pack()
r3.pack()
win.mainloop()