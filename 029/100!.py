# -------------------------------------------------------------------------------
# Name:        029 calculate 100!
# Purpose:     return the value of 100!
#
# Author:      Douglas Green
#
# Created:     10/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------
from tkinter import *


window = Tk()


def calc():
    factorial(100)


def factorial(n):
    if n <= 1:
        lbl.configure(text='1')
    n = n * factorial(n - 1)
    lbl.configure(text=str(n))



# UI elements
window.title("factorial 100")
btn = Button(text='Start', command=calc)
lbl = Label(text='Hit Start')
lbl.pack()
btn.pack()
window.mainloop()