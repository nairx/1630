from tkinter import *

def submit():
    msg = "Hello " + txtName.get()
    lblMsg = Label(root,text=msg)
    lblMsg.place(relx=0.05,rely=0.4)

def showForm():
    global root,txtName,btnSubmit,lblMsg
    root = Tk()
    root.geometry("900x500")
    root.option_add("*Font","aerial 14 bold")
    lblName = Label(root,text="Enter Name: ")
    lblName.place(relx=0.05,rely=0.05)
    txtName = Entry(root)
    txtName.place(relx=0.2,rely=0.05)
    btnSubmit = Button(root,text="Submit",command=submit)
    btnSubmit.place(relx=0.05,rely=0.2)
    root.mainloop()

showForm()