class Employee:
    
    language = "Py"#here language and salary are the class attributes because it directly belongs to the class..
    salary = 1200000

harry = Employee()
harry.name = "Harry"#this is an object attribute..(or instannce attribute)
print(harry.salary , harry.language)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name , rohan.salary , rohan.name)

#here name is the object attributes and the language and salary
#is the class attributes as they direclty belongs to the class..


