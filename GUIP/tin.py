import tkinter
from tkinter import * # its important if it says Tk is not defined

win = Tk() # creating the window where every thing is between the window and the main loop
def pr():
    print('hi')
win.geometry('400x400')
b = Button( win, text = ' button') # decalre a button
#b.pack()
# it shows the button because its nor enough to declare it also you cant control the location

b2 = Button(win,text="buttoon2" , command=pr, padx = 10 , pady=10, activeforeground="red")
#b2.grid(row=1, column=1)
# we use this order inorder tobe able to show the button on a spicific place using grids
# you cant use PACK and GRID in the same window
# to make a buttom do any thinf you beed to define a commend that it executes and you need to create than command as a function
#padx and pady to control the size of the button
#activeforeground to gice the btton color when pressed
b2.place(x=100,y=200) # we place it by using pixels
win.mainloop()