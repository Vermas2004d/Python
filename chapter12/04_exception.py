

try:
    a = int(input("Enter the number: "))
    print(a)

except ValueError as v:
    print("heyy")
    print(v)

except Exception as e:
    print(e)


print("you are done")