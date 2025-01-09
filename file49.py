class Shape:
    def area(self):
        print("Hello")

class Square(Shape):
    def area(self):
        print("Good Morning")

s = Square()
s.area() #Polymorphism - Method Overriding