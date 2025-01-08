import os
import pickle
os.chdir('D:/temp')
txt = input("Enter data: ")
f = open("myfile.pkl",'wb')
# f.write(txt)
pickle.dump(txt,f)
# f.close()