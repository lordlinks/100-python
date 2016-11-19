# -------------------------------------------------------------------------------
# Name:        017 count vowels in a string
# Purpose:
#
# Author:      Douglas Green
#
# Created:     10/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------
import tkinter


def calc():
    v = 0
    # get the value from the entry window
    x = ent.get()
    # convert all characters to lower case so we don't miss any
    x = x.lower()
    for y in x:
        # for any of the vowels add 1 to the running counter
        if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':
            v += 1
        else:
            pass
    # make the counter a string instead of int
    v = str(v)
    # write the text and count to the label under the button
    lbl2.configure(text="Your phrase contains "+v+" vowels")


window = tkinter.Tk()
# name the window
window.title("Vowel Counter")
# the UI elements
lbl = tkinter.Label(window, text="Enter a Word or sentence")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Calculate", command=calc)
lbl2 = tkinter.Label(window, text="Your phrase contains 0 vowels")
# stack the elements on top of each other
lbl.pack()
ent.pack()
btn.pack()
lbl2.pack()
window.mainloop()
