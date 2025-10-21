#Write a python function  to remove a given word from a list  and strip it at the same time..


def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))#strip will remove the heading and trailing word from the item..
    return n
    
l = ["Haanrry" , "Rohan" , "anShubham" , "an"]

print(rem(l, "an"))


