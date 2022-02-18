from tkinter import *

win = Tk()
win.geometry('200x100')

def getkey(e):
    print(e.keycode)

win.bind("<Key>", getkey)

win.mainloop()
