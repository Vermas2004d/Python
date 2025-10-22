def myFunc():
    print("hello world")

    


#If i am running this code with the help of this file name,
#then the  __name__ function will give the __main__ to us,
#but if we are executing this file by importing it in the other file
#then it will give us the filename from where we are importing it..

if __name__ == "__main__":
    #if this code is direclty executed by running the file its present in..
    print("we are direclty running this code")
    myFunc()
    print(__name__)


