from tkinter import *
import mysql.connector

# Mysql Connection:
def connect():
        uname = nameTF.get()
        uroll = rollTF.get()
        mydb1=mysql.connector.connect(host="localhost",user="root",passwd="",database="mydb")
        mycursor = mydb1.cursor()
        mycursor.execute("INSERT INTO students (name, rollno) VALUES (%s, %s)", (uname, uroll));
        mydb1.commit();


master = Tk();
v = IntVar();
nameL = Label(master, text="Name: ")
rollL = Label(master, text="Roll No: ")

nameTF = Entry(master);
rollTF = Entry(master);

submitBtn = Button(master, text="Submit", command=connect);

# grid ...

nameL.grid(row=0, column=0);
rollL.grid(row=1, column=0);

nameTF.grid(row=0, column=1);
rollTF.grid(row=1, column=1);

submitBtn.grid(row=2);

master.mainloop();
