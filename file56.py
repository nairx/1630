import threading
from time import sleep
def f1():
    for i in range(3):
        sleep(2)
        print("f1",i)
def f2():
    for i in range(3):
        sleep(1)
        print("f2",i)
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Completed Successfully")

