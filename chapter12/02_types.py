from  typing import List, Union , Dict , Tuple

#List of integers
numbers: List[int] = [1,2,3,4,5]

#Tuple of a string and a integer
person: Tuple[str , int] = ("Alice" , 30)

#Dictionary with string keys and integer values
scores: Dict[str , int] = {"Alice": 90 , "Bob": 85}

#Union type for variables that can hold multiple types
identifier: Union[int , str] = "ID123"
identifier = 12345 #Also valid

#These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance


n : int = 5

name : str = "Harry"


#for functions:
def sum(a : int , b : int) -> int:
    return a+b

result = sum(3 , 6)
print(result)

#We also have the advance type hints:
#Python's typing module provides more advanced type hints, such as List , Tuple , Dict,
# and Union
#-->You can import List , Tuple and Dict types from the typing module like this:
#from typing import List, Tuple, Dict, Union

