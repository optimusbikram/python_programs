#program for enetering a value and get the type of the value


def gettype(value):
    if(type(value)== int):
        print("{} is of type int".format(value))
    elif(type(value) == float):
        print("{} is of type float".format(value))
    elif(type(value) == str):
        print("{} is of type string".format(value))
    elif(type(value) == bool):
        print("{} is of type boolean".
              format(value))
    elif(type(value)==list):
        print("{} is of type list".format(value))
    elif(type(value)==tuple):
        print("{} is of type tuple:".format(value))
    elif(type(value)==dict):
        print("{} is of type dict".format(value))
    elif(type(value)==set):
        print("{} is of type set".format(value))
    elif(type(value)==frozenset):
        print("{} is of type frozenset".format(value))
    elif(type(value)==complex):
        print("{} is of type complex".format(value))
    elif(type(value)==bytes):
        print("{} is of type bytes".format(value))
    elif(type(value)==bytearray):
        print("{} is of type bytearray".format(value))
    else:
        print("{} is of unknown type".format(value))

#main logic

gettype(10)
gettype(20.5)
gettype("Roosum")       
gettype(True)
gettype([10,20,30])
gettype((10,20,30))
gettype({10:"Python",20:"Java",30:"c++"})
gettype({10,20,30})
gettype(frozenset([10,20,30]))  
gettype(10+20j)
gettype(b"Hello")
gettype(bytearray(b"Hello"))
gettype(None)
