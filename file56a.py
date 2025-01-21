from time import sleep
def f1():  
    for i in range(3):
        sleep(2)
        print("f1",i)
def f2(): 
    for i in range(3):
        sleep(1)
        print("f2",i)
# 1 milli second
f1() #6 seconds
f2() #3 seconds
print("Program Completed Successfully")