class Mammal:
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")
        
d = Dog()
d.bark()
d.walk() #Inheritance



