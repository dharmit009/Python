import mysql.connector
from tkinter import *

def myfunc():
    name=ename.get();
    addr=eaddr.get();
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="test2")

    mycursor = con.cursor()
    sql = "Insert into customers(Name, Address) Values('"+name+"' , '"+addr+"')"
    print(sql)
    mycursor.execute(sql)
    con.commit()
    con.close()
    

master = Tk()

label1 = Label(master, text="Name: ")
label2 = Label(master, text="Address: ")

ename = Entry(master)
eaddr = Entry(master)

button1 = Button(master, text="Submit", command=myfunc)

# Gridding ...
label1.grid(row=0, column=0)
ename.grid(row=0, column=1)

label2.grid(row=1, column=0)
eaddr.grid(row=1, column=1)

button1.grid(row=3, column=2)
master.mainloop()



