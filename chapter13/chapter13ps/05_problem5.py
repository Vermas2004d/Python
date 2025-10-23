

from functools import reduce

l = [1,23,42,21,56,32,87,65]


def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater  ,l))



