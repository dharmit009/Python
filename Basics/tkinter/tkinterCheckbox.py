from tkinter import *

window = Tk();
def hobby():
    if musicVar == 1 and photoVar == 0:
        label2.config(text="I like to mistento music")
    elif musicVar == 0 and photoVar == 1:
        label2.config(text="I Like Photography.")
    elif musicVar == 1 and photoVar == 1:
        label2.config(text="I like to do both.")
    else: 
        label2.config(text="Error! [E]: ")



musicVar = IntVar();
photoVar = IntVar();

cmblist1 = Checkbutton(window, text="Music", variable=musicVar)
cmblist2 = Checkbutton(window, text="Photo", variable=photoVar)

label1 = Label(window, text="Select Your Hobby");
label2 = Label(window, text="");

submit = Button(window, text="Submit", command=hobby)

label1.grid(row=0)
cmblist1.grid(row=1, column=0)
cmblist2.grid(row=2)
label2.grid(row=4, column=0)
submit.grid(row=4, column=0)

window.mainloop()
