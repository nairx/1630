import os
folders = os.listdir('D:/demo')
while True:
    for i in folders:
        print(i)
    ch = input("Enter folder name: ")
    print(os.listdir(f'D:/demo/{ch}'))
    choice=input("Do you want to continue?(y/n)")
    if choice != 'y':
        break
