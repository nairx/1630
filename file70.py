from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mypythondb"
)
mycursor = mydb.cursor()


def saveForm():
    name = txtName.get()
    email = txtEmail.get()
    sql = "insert into customers(name,email) values(%s,%s)"
    value = (name,email)
    mycursor.execute(sql,value)
    mydb.commit()
    txtName.delete(0,100)
    txtEmail.delete(0,100)
    

def showForm():
    global root,txtName,txtEmail
    root = Tk()
    root.geometry("900x500")
    root.title("My Application")
    root.option_add("*Font","aerial 14 bold")
    lblName = Label(root,text="Enter Name:")
    lblName.place(relx=0.05,rely=0.05)
    txtName = Entry(root)
    txtName.place(relx=0.2,rely=0.06)
    lblEmail = Label(root,text="Enter Email:")
    lblEmail.place(relx=0.05,rely=0.15)
    txtEmail = Entry(root)
    txtEmail.place(relx=0.2,rely=0.15)
    btnSubmit = Button(root,text="Submit",command=saveForm)
    btnSubmit.place(relx=0.05,rely=0.25)
    root.mainloop()

showForm()