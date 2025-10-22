
#Finally is very useful in the functions , because when we return the function in try or except block
# then finally also executed but if we are not using the finally keyword then it will not be performed ..


def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return 

    except Exception as e:
        print(e)
        return 

    finally:
        print("Hey i am inside of finally")

main()



