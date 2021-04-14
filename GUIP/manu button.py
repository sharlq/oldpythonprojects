import tkinter
from tkinter import * # its important if it says Tk is not defined
from tkinter import messagebox # wee need to import this to create message boxs
win =Tk()

mb = Menubutton(win,text='file')
mb.grid()
#what does those mean
mb.menu = Menu(mb)
mb['menu'] = mb.menu
#
x1=IntVar()
x2=IntVar()

mb.menu.add_checkbutton(label='open',variable=x1)
mb.menu.add_checkbutton(label='close',variable=x2)
win.mainloop()