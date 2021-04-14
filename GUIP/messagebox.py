import tkinter
from tkinter import * # its important if it says Tk is not defined
from tkinter import messagebox # wee need to import this to create message boxs
win =Tk()
def hello():
    messagebox.showinfo('from computer','hello there')
b= Button(win,text='pop up',command=hello)
b.pack()
win.mainloop()