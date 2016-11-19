# -------------------------------------------------------------------------------
# Name:         Binomial Evaluator
# Purpose:      Find the binomial coefficients to a statement
#
# Author:       Douglas Green
#
# Created:      11/12/2014
# Copyright:    (c) Douglas Green 2014
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------
import tkinter
import sympy


def calc():
    x, y = sympy.symbols("x y")
    formula = ent.get()
    formula = s(formula.expand())
    lbl2.configure(text=str(formula.replace("**", "^")))


window = tkinter.Tk()
window.title("Binomial Expansion")
lbl = tkinter.Label(window, text="please insert a formula using x and y as your variables")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="command", command=calc)
lbl2 = tkinter.Label(window)
lbl.pack()
ent.pack()
btn.pack()
lbl2.pack()


window.mainloop()