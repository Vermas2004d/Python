a = 89 #global variable

def fun():
    global a
    a = 3
    print(a)

fun()
print(a)


