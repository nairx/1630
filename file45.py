class Calc:
    def __init__(self,x,y): #constructor
        self.x = x
        self.y = y
    def add(self):
        print(self.x+self.y)
    def subtract(self):
        print(self.x-self.y)
    def multiply(self):
        print(self.x*self.y)
    def divide(self):
        print(self.x/self.y)

c1 = Calc(6,2)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()
    