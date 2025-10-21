class Calculator:
    def __init__(self , num):
        self.num = num
    def square(self):
        return self.num * self.num
    def cube(self):
        return self.num * self.num * self.num
    def sqroot(self):
        return pow(self.num , 1/2)
    @staticmethod
    def greet():
        print("Good evening!")

s1 = Calculator(100)
result = s1.sqroot()
print(result)

s1.greet()



        