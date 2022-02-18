from tkinter imoprt *

win = Tk()

def getkey(e):
    print(e.keycode)

win.bind("<Key>", getkey)

win.mainloop()
