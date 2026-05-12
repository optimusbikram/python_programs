
#program for finding sum and average of list of values using function

def readvalues():
    n=int(input("Enter number of values: ")) #number of values to be entered
    values=[]
    for i in range(n):
        values.append(float(input("Enter value: ")))
    return values


def sumavg(values):
    total=sum(values)
    average=total/len(values)
    return total, average

def main():
    values=readvalues()
    total,average=sumavg(values)
    print("Sum: ",total)
    print("Average: ",average)
if __name__=="__main__":  
    main()
