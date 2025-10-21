
class mine:
    a = "madhav"

o = "sarthak"
object = mine()
print(object.a)#prints the class attribute because instance attribute is not present


object.a = o #Instance attribute is set

print(object.a) #Prints the instance attribute because instance attribute is present
#No the class attribute does not changes, it only changes the object instant value for that class variable..


print(mine.a) #still gives the madhav as output..



