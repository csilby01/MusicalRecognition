from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x500')
root.title("Musical Recognition")


def pic():
    print("a")

def login():
    b1 = ttk.Button(frm, text="Take Picture", command= pic).grid(column=2, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=7)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Musical Recognition").grid(column=0, row=0)

b0=ttk.Button(frm, text = "Login", command = login).grid(column=2, row=1)


root.mainloop()