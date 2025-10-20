num1 = int(input("Enter the first no: "))
num2 = int(input("Enter the second no: "))
num3= int(input("Enter the third no: "))
num4= int(input("Enter the fourth no: "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("Num1 is largest")
elif(num2>= num1 and num2 >= num3 and num2 >= num4):
    print("Num2 is largest")
elif(num3>= num1 and num3 >= num2 and num3 >= num4):
    print("Num3 is largest")
elif(num4>= num1 and num4 >= num2 and num4 >= num3):
    print("Num4 is largest")
else:
    print("some another number is largest")
