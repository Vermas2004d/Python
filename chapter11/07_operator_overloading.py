class Number:
    def __init__(self , n):
        self.n = n

    def __add__(self , num):
        return self.n + num.n


n = Number(1)
m = Number(2)
print(n+m)

#Other dunder operator overloading methods in python:
# __str__() --> used to set what gets displayed upon calling str(obj)
# __len__() --> used to set what gets displayed upon calling.  __len__() or len(obj)

#Agin check the operator overloading functions..
