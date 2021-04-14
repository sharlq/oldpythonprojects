import tkinter
from tkinter import * # its important if it says Tk is not defined

win = Tk()
win.geometry('600x600')
c = Canvas(win, height = 400 ,width = 400, bg="blue") # you can add thing inside the canvas
coord = 10 , 50 ,240 , 210
arc = c.create_arc(coord,start=0,extent=100, fill= 'red') # most of those things are figures and images
line = c.create_line(10,10,200,200,fill="green")


c.pack() # also in Canvas declaring is different from showing you need to declare them show

win.mainloop()