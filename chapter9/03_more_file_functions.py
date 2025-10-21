
f= open("file.txt")

# lines = f.readlines()

# print(lines , type(lines))#return the lines in the list
# f.close()


# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))

# line6 = f.readline()
# print(line6, type(line6))

# line7 = f.readline()
# print(line7, type(line7))


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()





