'''
***
* *
***
'''

#written by me:
# num = int(input("Enter the number: "))
# for i in range(1,num+1):
#     if(i%2!=0):
#         print("*" * num)
#     else:
#         print("*" * (2*i-1) , end="")
#         print(" "*1, end="")
#         print("")


#by the teacher
n= int(input("Enter the number: "))
for i in range(1 , n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
    print("")
    



