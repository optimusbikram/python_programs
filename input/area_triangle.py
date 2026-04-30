#calculate area of o ftriangle when height and base is given
#taking input from user
# and also calculate area of triangle when three sides are given


#taking input from user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
#calculating area of triangle
area = 0.5 * base * height
#printing the result
print("Area of the triangle is: ", area)
#taking input from user
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the traingle: "))
side3 = float(input("Enter the third side of the traingle: "))
#calculating area of triangle using heron's formula
s = (side1+ side2 + side3) /2
area_heron = (s*(s-side1)*(s-side2)*(s-side3))**0.5
#printing the result
print("Area of the treiangle using heron's formula is : ",area_heron)