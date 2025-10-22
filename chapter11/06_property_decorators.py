
class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property # getter 
    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    @fullname.setter # setter
    def fullname(self, value): 
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

#the property decorator will be here using the concept of the abstraction and the encapsulation..
# here it feels we are making the fullname as the function but actually by seeing it looks like
# we are making the instance variable
#That is the beauty of the property decorator

e.fullname = "Madhav Verma"
print(e.fname , e.lname)

e.show()

