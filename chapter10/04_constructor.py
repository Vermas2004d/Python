class Employee:
    language = "Python" #This is a class attribute
    salary = 1200000

    def __init__(self, name , salary , language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod #now it is a static method--> now there is no need to take the object
    def greet():
        print(f"Good morning")


harry = Employee("Harry" , 13000000 , "JavaScript")
# harry.name = "Harry"
print(harry.name , harry.salary, harry.name)

rohan = Employee()

