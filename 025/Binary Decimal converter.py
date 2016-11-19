# -------------------------------------------------------------------------------
# Name:         025 Decimal to Binary Converter
# Purpose:      Take a number and select view of that number in different
# binary notations
#
# Author:       Douglas Green
#
# Created:      13/10/2014
# Copyright:    (c) Douglas Green 2014
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------
from tkinter import *


window = Tk()
window.minsize(width=200, height=180)
v = IntVar()
v.set(1)


def unsigned():
    """
    Activated by sel() and returns the unsigned notation of the input number
    changes lbl2 to be the formatted string
    """
    x = ent.get()
    try:
        x = int(x)
        x = '{0:b}'.format(x)
        x = zadder(x, False)
        lbl2.configure(text=x)
    except ValueError:
        lbl2.configure(text="You didn\'t input a positive integer")


def signed():
    """
    Activated by sel() figures out if a number is negative or positive, then
    changes lbl2 to be the formatted string
    """
    try:
        x = int(ent.get())
        if x >= 0:
            x = zadder('{0:b}'.format(x), False)
            lbl2.configure(text=x)
        else:
            x = zadder('{0:b}'.format(x), True)
            lbl2.configure(text=x)
    except ValueError:
        lbl2.configure(text="You didn\'t input an integer")


def ones():
    """
    Activated by sel() and returns the ones compliment representation of a number
    changes lbl2 to be the formatted string
    """
    try:
        x = int(ent.get())
        if x >= 0:
            x = int(ent.get())
            x = zadder('{0:b}'.format(x), False)
            lbl2.configure(text=x)
        else:
            x = '{0:b}'.format(x)
            x = x[1:]
            x = zadder(x, False)
            x = "0"+x
            x = x.replace("0", "x")
            x = x.replace("1", "0")
            x = x.replace("x", "1")
            lbl2.configure(text=x)
    except ValueError:
        lbl2.configure(text="You didn\'t input an integer")


def twos():
    """
    Activated by sel() and returns the twos compliment representation of a number
    changes lbl2 to be the formatted string
    """
    try:
        x = int(ent.get())
        if x >= 0:
            x = int(ent.get())
            x = zadder('{0:08b}'.format(x), False)
            lbl2.configure(text=x)
        else:
            x = '{0:b}'.format(x)
            x = x[1:]
            x = zadder(x, False)
            x = "0"+x
            x = x.replace("0", "x")
            x = x.replace("1", "0")
            x = x.replace("x", "1")
            x = int(x, 2) + 1
            x = '{0:b}'.format(x)
            lbl2.configure(text=x)
    except ValueError:
        lbl2.configure(text="You didn\'t input an integer")


def zadder(num, neg):
    """
    :param num: input binary number as string
    :param neg: boolean; if the number is negative input true
    :return: formatted number as string with sign bit and zero spacing
    """
    x = num
    y = 8 - (len(num) % 8)
    if neg:
        if y == 8:
            return "1" + x
        else:
            return "1" + ("0" * (y - 1)) + x
    else:
        if y == 8:
            return x
        else:
            return (y * "0") + x


def sel():
    """
    :return: none
    Global variable is checked and correct metod is used based on selection
    """
    x = v.get()
    if x == 1:
        unsigned()
    elif x == 2:
        signed()
    elif x == 3:
        ones()
    elif x == 4:
        twos()
    else:
        print("error")


# give the window a title
window.title("Decimal To Binary")
# the UI elements
lbl = Label(window, text="Enter a integer (unsigned must be positive)", pady=10)
ent = Entry(window)
rdo0 = Radiobutton(window, text="Unsigned", variable=v, value=1)
rdo1 = Radiobutton(window, text="Signed", variable=v, value=2)
rdo2 = Radiobutton(window, text="One\'s Compliment", variable=v, value=3)
rdo3 = Radiobutton(window, text="Two\'s Compliment", variable=v, value=4)
btn = Button(window, text="Calculate", command=sel)
lbl2 = Label(window, text="Nothing to see here", pady=10)
# Stack the UI elements on top of each other
lbl.grid(row=0, column=0, columnspan=2)
ent.grid(row=1, column=0, columnspan=2)
rdo0.grid(row=2, column=0)
rdo1.grid(row=2, column=1)
rdo2.grid(row=3, column=0)
rdo3.grid(row=3, column=1)
btn.grid(row=4, column=0, columnspan=2)
lbl2.grid(row=5, column=0, columnspan=2)
window.mainloop()