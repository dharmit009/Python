from tkinter import *

master = Tk()

mm = Menu(master)
mabout = Menu(mm)
mabout.add_command(label="test1")
mabout.add_command(label="test2")
mabout.add_command(label="test3")
mm.add_cascade(menu=mabout, label="About")

master.config(menu=mm)
master.geometry("700x500")
master.mainloop()
