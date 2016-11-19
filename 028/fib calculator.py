# -------------------------------------------------------------------------------
# Name:        Fibonacci Number Calculator
# Purpose:      Returns the fibb numbers up to the limit you set
#
# Author:      Douglas Green
#
# Created:     10/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------

import math
import sys
import tkinter


def loop():
    p = 0
    try:
        p = int(ent.get())
    except ValueError:
        pass
    r = 0
    x = 1
    y = 1
    z = 0
    while r <= p:
        r += 1
        z = x+y
        x = y
        y = z
        if r%6 == 0:
            lbl0.configure(text=str(z))
            lbl0.pack()
        if r%6 == 1:
            lbl1.configure(text=str(z))
            lbl1.pack()
        if r%6 == 2:
            lbl2.configure(text=str(z))
            lbl2.pack()
        if r%6 == 3:
            lbl3.configure(text=str(z))
            lbl3.pack()
        if r%6 == 4:
            lbl4.configure(text=str(z))
            lbl4.pack()
        if r%6 == 5:
            lbl5.configure(text=str(z))
            lbl5.pack()


window = tkinter.Tk()
# name the window
window.title("Fibonacci Sequence Calculator")
# the UI elements
lbl = tkinter.Label(window, text="Enter a positive integer")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Calculate", command=loop)
lbl0 = tkinter.Label(window)
lbl1 = tkinter.Label(window)
lbl2 = tkinter.Label(window)
lbl3 = tkinter.Label(window)
lbl4 = tkinter.Label(window)
lbl5 = tkinter.Label(window)
# stack elements on each other
lbl.pack()
ent.pack()
btn.pack()
window.mainloop()