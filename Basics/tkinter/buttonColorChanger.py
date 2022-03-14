from tkinter import *

def emp():
    pass

def selection():
    selector = v.get()
    if selector == 1:
        lbl1.config(fg="Red")
    elif selector == 2:
        lbl1.config(fg="Blue")
    elif selector == 3:
        lbl1.config(fg="Green")
    else:
        lbl1.config()

master = Tk()

mm=Menu(master)
mm.add_command(label="file", command=emp)
mm.add_command(label="file1", command=emp)
mm.add_separator()

v = IntVar();

rb1 = Radiobutton(master, text="Red", variable=v, value=1, command=selection )
rb2 = Radiobutton(master, text="Blue", variable=v, value=2, command=selection,)
rb3 = Radiobutton(master, text="Green", variable=v, value=3, command=selection)

lbl1 = Label(master, text="Hello, World!!")

lbl1.pack()

rb1.pack()
rb2.pack()
rb3.pack()

master.geometry("500x700")
master.config(menu=mm)
master.mainloop()
