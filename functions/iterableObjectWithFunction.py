def dispvalues(iterable):
    print("The type of iterable is :",type(iterable))
    print("The values in the iterable are :")
    print("*"*50)
    print("The Length of the iterable is :",len(iterable))
    if isinstance(iterable,dict):
        for key,val in iterable.items():
            print("\t",key,"-->",val)
    else:
        for val in iterable:
            print("\t",val)

    
    print("*"*50)


#main program
lst=[10,"Roosum",20.5,True]
dispvalues(lst)
tpl = (10,"tuple",467567,"Python",67.90)
dispvalues(tpl)
d={10:"Python",20:"Java",30:"c++",40:"HTML"}
dispvalues(d)
