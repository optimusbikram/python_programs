a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# Perform multiplication
# Print the result 
print("The result of {} and {} multiplication is: {}".format(a, b, a * b))
print("---------------------------OR---------------------------")
print("MUL(%0.2f, %0.2f) = %0.4f" % (a, b,round(a * b, 4)))