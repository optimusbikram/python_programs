#program to find a multiplication table of a number using function

def multiplicationtable(n):
    if(n<0):
        print("Invalid input. Please enter a non-negative integer.")
        return
    elif(n==0):
        print("Multiplication table of 0 is always 0.")
        return
    else:
        print("Multiplication table of ", n)
        for i in range(1, 11):
             print("\t",n, "x", i, "=", n*i)
            

def main():
    number=int(input("Enter a number: "))
    multiplicationtable(number)

if __name__=="__main__":
    main()