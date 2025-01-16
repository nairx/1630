import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mypythondb"
)
mycursor = mydb.cursor()
while True:
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    sql = "insert into customers(name,email) values(%s,%s)"
    value = (name,email)
    mycursor.execute(sql,value)
    mydb.commit()
    print(mycursor.rowcount, " record inserted.")
    ch=input("Do you want to continue?(y/n)")
    if ch=='n':
        break