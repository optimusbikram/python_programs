#define a function for adding two numbers
def add_numbers(num1,num2): #function takes two formal parameters num1 and num2
    return num1+num2
#call the function and print the result
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = add_numbers(num1, num2) 
print("The sum of", num1, "and", num2, "is:", result)
