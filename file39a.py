import os
os.chdir("D:/temp")
with open('myfile.txt', 'r') as file:
    data = file.read()
    print(data)