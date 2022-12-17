from tkinter import *


def change():
    if r_var.get() == 0:
        lbl.config(bg='blue')
    elif r_var.get() == 1:
        lbl.config(bg='green')
    elif r_var.get() == 2:
        lbl.config(bg='red')


root = Tk()
r_var = IntVar()
r_var.set(0)
r1 = Radiobutton(text='Red', variable=r_var, value=2)
r2 = Radiobutton(text='Green', variable=r_var, value=1)
r3 = Radiobutton(text='Blue', variable=r_var, value=0)
btn = Button(text='Change', command=change)
lbl = Label(width=10, height=10, bg='Blue')
r1.pack()
r2.pack()
r3.pack()
btn.pack()
lbl.pack()
root.mainloop()
