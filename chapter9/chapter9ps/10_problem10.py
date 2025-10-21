# wipe put the content of the file using python..

with open("wipe.txt") as f:
    content = f.read()

with open("wipe.txt", "w") as f:
    content = content.replace(content , "")

