class Main:
    def f1(self):
        print("Hello World")
        

class Sub(Main):  #inheritance
    def f2(self):
        print("Good Evening")
        

s = Sub()
s.f1()
s.f2()