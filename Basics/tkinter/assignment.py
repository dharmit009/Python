from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb'
)

def add1():
    b = bname.get()
    a = aname.get()
    i = isbn.get()
    mycursor = mydb.cursor()
    sql = "Insert into book(bookname,authorname,isbn) Values('"+b+"' , '"+a+"','"+i+"')"
    lb.config(text="Data Inserted!!!")
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()

def display():
    mycursor = mydb.cursor()
    sql = "select * from book"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    n = 8
    for x in myresult:
        n = n +1
        Label(master, text=x).grid(row=n)

def search():
    b = s.get()
    mycursor = mydb.cursor()
    sql = "select * from book where bookname='"+b+"' or authorname ='"+b+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    n = 8
    for x in myresult:
        n = n +1
        Label(master, text=x).grid(row=n)

def delete():
    sel = lst.curselection()
    index= sel[0]
    value = lst.get(index)
    lst.delete(index)
    sql = "delete from book where bookname='"+value+"'"
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()


def update():
    sel = lst1.curselection()
    name = e1.get()
    index= sel[0]
    value = lst.get(index)
    sql = "Update book set bookname='"+name+"' where bookname='"+value+"'"
    mycursor.execute(sql)
    mydb.commit()
    mydb.close()

master =Tk()

Label(master, text="Book Name : ").grid(row=0)
bname = Entry(master)
bname.grid(row=0,column=1)
Label(master, text="Author Name : ").grid(row=1)
aname = Entry(master)
aname.grid(row=1,column=1)
Label(master, text="ISBN Code : ").grid(row=2)
isbn = Entry(master)
isbn.grid(row=2,column=1)
lb = Label(master, text="")
lb.grid(row=3)
lb1 = Label(master, text="")
lb1.grid(row=5)
b1=Button(master,text="Insert", command=add1)
b1.grid(row=3, column=1,sticky=E)
b2=Button(master,text="Display", command=display)
b2.grid(row=3, column=2,sticky=E)
Label(master, text="Search : ").grid(row=5)
s = Entry(master)
s.grid(row=5,column=1)
b3=Button(master,text="Search", command=search)
b3.grid(row=5, column=2,sticky=E)
Label(master, text="Select to delete : ").grid(row=10)
lst = Listbox(master)
mycursor = mydb.cursor()
sql = "select bookname from book"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    lst.insert(END,i[0])
lst.grid(row=10, column=1)
b4=Button(master,text="Delete", command=delete)
b4.grid(row=10, column=2,sticky=E)
Label(master, text="Select to Update : ").grid(row=11)
lst1 = Listbox(master)
mycursor = mydb.cursor()
sql = "select bookname from book"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    lst1.insert(END,i[0])
lst1.grid(row=11, column=1)
b4=Button(master,text="Update", command=update)
Label(master, text="Enter the Updated Book Name : ").grid(row=12)
e1= Entry(master)
e1.grid(row=12, column=1)
b4.grid(row=12, column=2,sticky=E)

master.mainloop()


