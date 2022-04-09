
from tkinter import *

master = Tk(); # create a window ...

Lb = Listbox(master)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()

master.geometry("300x700")
master.mainloop() # run in loop ...
