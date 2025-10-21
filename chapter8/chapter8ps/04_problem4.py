


def Sum(n):
    if(n == 1):
        return 1
    return n + Sum(n-1)

num = int(input("Enter the number: "))
result = Sum(num)
print(result)

