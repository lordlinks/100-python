# -------------------------------------------------------------------------------
# Name:        003 Temp Converter
# Purpose:
#
# Author:      Douglas Green
#
# Created:     10/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------
import tkinter


def f_to_c():
    # gets the value from the first input box
    f_c = int(ent.get())
    try:
        # performs the calculation and changes the label under the button to show the temp
        lbl2.configure(text=str(5/9*(f_c-32))+"C")
    except ValueError:
        print("error 1")


def c_to_f():
    # gets the value from the second input box
    c_f = int(ent2.get())
    try:
        # performs the calculation and changes the label under the button to show the temp
        lbl4.configure(text=str(c_f*(9/5)+32)+"F")
    except ValueError:
        print("error 2")


window = tkinter.Tk()
# name the window
window.title("Temp Converter")
# elements of the UI
lbl = tkinter.Label(window, text="Convert fahrenheit")
ent = tkinter.Entry(window)
lbl2 = tkinter.Label(window, text="0")
btn = tkinter.Button(window, text="Calculate", command=f_to_c)
lbl3 = tkinter.Label(window, text="Convert Celsius")
ent2 = tkinter.Entry(window)
lbl4 = tkinter.Label(window, text="0")
btn2 = tkinter.Button(window, text="Calculate", command=c_to_f)
# stack the elements on top of each other
lbl.pack()
ent.pack()
lbl2.pack()
btn.pack()
lbl3.pack()
ent2.pack()
lbl4.pack()
btn2.pack()
window.mainloop()