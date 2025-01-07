import os
os.chdir('D:/temp')
print("*** File Management ***")
while True:
    print("1.Write File")
    print("2.Read File")
    print("3.Delete File")
    print("4.Exit")
    ch=input("Enter Choice:")
    if ch=="1":
        f=open('myfile.txt','a')
        data=input("Enter data: ")
        f.write(data)
        f.close()
    elif ch=="2":
        f=open('myfile.txt','r')
        data = f.read()
        print(data)
        f.close()
    elif ch=="3":
        os.remove('myfile.txt')
    else:
        break


