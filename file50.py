class Employee:
    def __init__(self,name):
        self.__name = name
    def setName(self,n):
        self.__name=n
    def getName(self):
        return self.__name

e = Employee("John")
e.setName("Cathy")
print(e.getName()) #encapsulation - variable is protected inside class