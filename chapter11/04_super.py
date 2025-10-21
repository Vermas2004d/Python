#Super method:
# super() method is used to access the methods of super class in the derived class.



class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    def greet(self):
        print("hello")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        
        print("Constructor of manager")
    c= 3

# o = Employee()
# print(o.a)#prints the a attribute

# #print(o.b) #Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a , o.b)

o = Manager()
# print(o.a , o.b , o.c)

