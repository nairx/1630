import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="classicmodels"
)
mycursor = mydb.cursor()
mycursor.execute("select * from products")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)