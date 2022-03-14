from tkinter import *

master = Tk()

## main menu ...
mm = Menu(master)

mm.add_command(label="text1")
mm.add_command(label="text2")

## About submenu ...
mabout = Menu(mm)
mabout.add_command(label="text1");
mabout.add_command(label="text2");
mm.add_cascade(label="File", menu=mabout)


master.config(menu=mm)
master.geometry("700x500");
master.mainloop();
