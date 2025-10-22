
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b==0): 
    raise ZeroDivisionError("Hey our program is not meant to divide the numbers by zero")
    # here the program crashes
else:
    print(f"The division a/b is {a/b}")

print("you are alone")