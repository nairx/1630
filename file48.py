class MyClass:
    def greet(self,name=None,title=None):
        if name and title:
            return f"Hello {title}. {name}"
        elif name:
            return f"Hello {name}"
        else:
            return f"Hello"

c1 = MyClass()
txt = c1.greet()  #Polymorphism - method overloading
print(txt)
