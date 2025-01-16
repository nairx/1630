import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mypythondb"
)
mycursor = mydb.cursor()
# mycursor.execute("create table customers(name varchar(100),email varchar(200))")
sql = "insert into customers(name,email) values(%s,%s)"
value = ("John","john@email.com")
mycursor.execute(sql,value)
mydb.commit()
print(mycursor.rowcount, " record inserted.")