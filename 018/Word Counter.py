# -------------------------------------------------------------------------------
# Name:        018 Word Counter
# Purpose:
#
# Author:      Douglas Green
#
# Created:     11/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------
import tkinter


def splitter():
    # get the phrase from the entry window
    words = ent.get()
    # split the string into a list of the words in it
    words = words.split()
    # count the list of words and and make the number a string
    c = str(len(words))
    # overwrite the label under the button to tell you how many words
    lbl2.configure(text="there are "+c+" words in the phrase")


window = tkinter.Tk()
# name the window
window.title("Word Counter")
# the UI elements
lbl = tkinter.Label(window, text="Enter a series of words")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Calculate", command=splitter)
lbl2 = tkinter.Label(window, text="There are 0 words in the phrase")
# stack elements on top of each other
lbl.pack()
ent.pack()
btn.pack()
lbl2.pack()
window.mainloop()