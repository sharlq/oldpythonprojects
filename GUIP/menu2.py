import tkinter
from tkinter import * # its important if it says Tk is not defined

win =Tk()
def saynothing():
    file = Toplevel(win)
    button = Buttom(file,text='do nothing')
    button.pack()

menubar = Menu(win)
filemenu = Menu(menubar)
filemenu.add_command(label='new window',command=saynothing)
filemenu.add_command(label='new file',command=saynothing)
filemenu.add_command(label='open',command=saynothing)
filemenu.add_separator()
filemenu.add_command(label='close',command=saynothing)
filemenu.add_command(label='destroy',command=saynothing)
filemenu.add_command(label='gas champers',command=saynothing)
filemenu.add_separator()
filemenu.add_command(label='exit',command=win.quit())

menubar.add_cascade(label='file',menu=filemenu)
editmenu=Menu(menubar)
win.config(menu=menubar)

win.mainloop()