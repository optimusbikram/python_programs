#4th approach for using functions in python
def sumoperation():
    a=int(input("Enter the first number: "))
    b =int(input("Enter the second number: "))
    sum=a+b
    return sum, a,b
print("Welcome to the sum operation program!")
sum, a, b = sumoperation()
print("The sum of {}, and {}, is : {}".format(a, b, sum))
print("-------------------------------------------")
res=sumoperation()
print(type(res))
print("The sum of {}, and {}, is : {}".format(res[0],res[1], res[2]))

