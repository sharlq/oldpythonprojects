import tkinter
from tkinter import * # its important if it says Tk is not defined
from functools import partial # its needed for the ability to access the function
win =Tk()
def sum(label,x1,x2):

    n1 = (x1.get()) # you must geet that data from entry by this order
    n2 = (x2.get())
    summ = int(n1) + int(n2)
    label.config(text = "sum is : %d" %summ)
    return

x1= StringVar()
x2= StringVar()

L= Label(win,text="first number")
L.grid(row=1,column=0)
e=Entry(win, textvariable=x1) # a box to enter info
e.grid(row=2,column=0)

L1= Label(win,text="first number")
L1.grid(row=1,column=1)
e1=Entry(win,textvariable=x2)
e1.grid(row=2,column=1)

label= Label(win)
label.grid(row=4,column=4)

sum = partial(sum,label,x1,x2) # inorder to access the function we need to use this order and we need to import its library

button = Button(win,text="calculate",command=sum)
button.grid(row=2,column=3)

#t = Text(win) # text box that has written info and you can write on it
#t.insert(INSERT,'hello') # to put a text in the text box
#t.pack()
win.mainloop()