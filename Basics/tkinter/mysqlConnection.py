import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test2")

mycursor = con.cursor()

# mycursor.execute("CREATE TABLE customers (Name varchar(255), Address varchar(255))");
print("Table Created Successfully")

sql = "Insert into customers(Name, Address) Values('TestEr' , 'New York City')"
mycursor.execute(sql)
con.commit()

con.close()
