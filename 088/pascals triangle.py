# -------------------------------------------------------------------------------
# Name:        088 Pascals Triangle
# Purpose:     calculates pascals triangle and prints to GUI
#
# Author:      Douglas Green
#
# Created:     11/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------
import math
import tkinter


# Make the global variable frm so that it can be changed and destroyed
frm = None


def start():
    global frm
    # get the levels from the entry widget
    i = 0
    x = ent.get()
    # destroy the frame and make a new one so we don't double up on results
    try:
        # if frame doesn't exist yet ie the first time don't try to destroy it.
        frm.destroy()
    except AttributeError:
        pass
    frm = tkinter.Frame(window)
    frm.pack(pady=10)
    try:
        # check to make sure that you have entered a integer
        x = int(x) - 1
        if x < 0:
            # if the integer is negative then don't calculate and end.
            pass
        while i <= x:
            # create label within the frame and pack them one underneath the other
            lblx = tkinter.Label(frm, text=str(itestep(i)))
            lblx.pack()
            # this iterator is here to count up to the limit of lines needed
            i += 1
    except ValueError:
        pass


def itestep(x):
    r = 0
    string = ''
    row = []
    count = 0
    while r <= x:
        # where the magic happens, this appends the integers for the elements to the list
        row.append(int(math.factorial(x) / (math.factorial(r) * math.factorial(x - r))))
        # this iterator is here to stop the loop
        r += 1
    for x in row:
        # this iterator is here to check for the last element so we don't add the , at the end
        count += 1
        if count == r:
            # this nicely formats the output so it's not just a list
            string += str(x)
        else:
            string += str(x) + ", "
    return string


window = tkinter.Tk()
window.title("Pascals Triangle Generator")
lbl = tkinter.Label(window, text="How many levels would you like to generate?")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Calculate", command=start)
lbl.pack()
ent.pack()
btn.pack(pady=10)
window.mainloop()