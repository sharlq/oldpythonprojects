import tkinter
from tkinter import * # its important if it says Tk is not defined

win =Tk()
s = Scale(win)
s.pack()

sb=Spinbox(win, from_ =0,to=10)
sb.pack()

scrolbar=Scrollbar(win)
list= Listbox(win,yscrollcommand=scrolbar.set)
for lin in range(100):
    list.insert(END, 'this is line no'+str(lin))

list.pack()
win.mainloop()