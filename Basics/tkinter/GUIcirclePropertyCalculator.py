from tkinter import *

def calc():
    r=int(radF.get())
    print(r);
    a = r*r*3.14;
    c = 2*3.14*r;
    areF.insert(0, a);
    cirF.insert(0, c);

def clear():
    radF.delete(0,100);
    areF.delete(0,100);
    cirF.delete(0,100);
    
    

master = Tk();

radL = Label(master, text="Radius: ");
areL = Label(master, text="Areaa: ");
cirL = Label(master, text="Circumference: ");

radF = Entry(master)
areF = Entry(master)
cirF = Entry(master)

clearBtn = Button(master, text="Clear", command=clear);
calBtn   = Button(master, text="Calculate", command=calc);

# grid ...

radL.grid(row=0, column=0);
areL.grid(row=1, column=0);
cirL.grid(row=2, column=0);

radF.grid(row=0, column=1);
areF.grid(row=1, column=1);
cirF.grid(row=2, column=1);

clearBtn.grid(row=4, column=0);
calBtn.grid(row=4, column=1);


master.mainloop()

