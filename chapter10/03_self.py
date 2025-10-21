

#Self Parameter:
# self refers to the instance of the class. It automatically passed with a function call
# from an object.


class Employee:
    language = "Python" #This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod #now it is a static method--> now there is no need to take the object
    def greet():
        print(f"Good morning")



harry = Employee()
harry.language = "Javascript" #This is an instance attribute
# harry.getInfo() --> Converted it into the Employee.getInfo(harry)
#So we have to pass the self parameter in the function that it in the class..
#becuase self is already assined in the formal argument place but we have 
#to send some parameter in the actual argument place..

harry.getInfo()
harry.greet()