#Write a program to find out whether the files identical and matches the content of another file.

with open("this.txt") as f:
    content = f.read()

with open("poem.txt" , "r") as f:
    content2 = f.read()

if(content == content2):
    print("Content is matched!")
else:
    print("Content mismatched!")

