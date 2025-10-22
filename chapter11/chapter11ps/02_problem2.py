
# Create a  class "Pets" from a class "Animals" and further create a class "Dog" from 
# "Pets". Add a method 'bark' to class "Dog"

class Animals:
    def __init__(self):
        print("I am a animal")


class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("I am a Pet")


class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("I am a Dog")

    def bark(self):
        print("Dog is barking")


# o1 = Animals()
# o2 = Pets()
o3 = Dog()
o3.bark()


