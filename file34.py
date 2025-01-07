import os
os.chdir('D:/temp')
f=open('myfile.txt','a')
while True:
    name=input("Enter Name:")
    age=input("Enter Age: ")
    phone=input("Enter Phone:")
    f.write(f"\n{name},{age},{phone}")
    ch=input("Continue? (y/n)")
    if ch=='y':
        continue
    else:
        break
f.close()
    