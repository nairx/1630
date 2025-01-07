import os
os.chdir('D:/')
os.mkdir("temp")
os.chdir('D:/temp')
f = open('myfile.txt','w')
f.write("This is a sample file.")
f.close()
