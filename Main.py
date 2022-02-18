from tkinter import *

win = Tk()

def getkey(e):
    print(e.keycode)

win.bind("<Key>", getkey)

win.mainloop()
