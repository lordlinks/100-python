# -------------------------------------------------------------------------------
# Name:         002 Higher or lower / heads or tails
# Purpose:      See if your guess is the same as the randomly generated answer
#
# Author:       Douglas Green
#
# Created:      28/01/2015
# Copyright:    (c) Douglas Green 2015
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------

from tkinter import *

window = Tk()


# variables for storing image
image_p = PhotoImage(file="Head.gif")
image_c = PhotoImage(file="Tail.gif")


# give the window a title
window.title("Heads or Tails")
# UI Elements
lbl1 = Label(window, text="HEADS or TAILS", pady=10)
lbl2 = Label(window, text="YOU", pady=10)
lbl3 = Label(window, text="COMPUTER", pady=10)
pic1 = Label(window, image=image_p)
lbl4 = Label(window, text="TIME")
lbl5 = Label(window, text="0")
pic2 = Label(window, image=image_c)
score_p = Label(window, text="0")
score_c = Label(window, text="0")
w_l = Label(window)
# Stack elements onto window using grid system
lbl1.grid(row=0, column=0, columnspan=3)
lbl2.grid(row=1, column=0)
lbl3.grid(row=1, column=2)
pic1.grid(row=2, column=0, rowspan=2)
lbl4.grid(row=2, column=1)
lbl5.grid(row=3, column=1)
pic2.grid(row=2, column=2, rowspan=2)
score_p.grid(row=4, column=0)
score_c.grid(row=4, column=2)
w_l.grid(row=5, column=0, columnspan=3)

window.mainloop()