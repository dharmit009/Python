from tkinter import *
window = Tk();
window.title("ADDER");

def summer():
    num1 = enum1.get();
    num2 = enum2.get();
    label3.config(text="Add = "+str(int(num1)+int(num2)))


label1 = Label(window, text="Enter Number 1: ")
label2 = Label(window, text="Enter Number 2: ")
label3 = Label(window, text="Add = ")

enum1 = Entry(window);
enum2 = Entry(window);

out = Button(window, text="Add", command=summer)

# <<< GRIDDING >>>
label1.grid(row=0, column=0)
enum1.grid(row=0, column=1)

label2.grid(row=1, column=0)
enum2.grid(row=1, column=1)

label3.grid(row=2, column=0)

out.grid(row=5, column=0)



window.mainloop();

