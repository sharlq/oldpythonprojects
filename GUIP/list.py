import tkinter
from tkinter import * # its important if it says Tk is not defined
from functools import partial # its needed for the ability to access the function
from tkinter import messagebox
win =Tk()

win.title('first')
top = Toplevel()
top.title('second')
lb = Listbox(win)
lb.insert(1,"python")
lb.insert(2,"c")
lb.insert(3,"java")
lb.pack()

win.mainloop()