#area of rectangle and perimeter of rectangle 
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle:"))
#calculate the area and perimeter of the rectangle
area = length * width
perimeter = 2 * (length + width)
#display the result
print("="*50)
print("The area of the reactangle is: {}".format(area))
print("The perimeter of the rectangle is: {}".format(perimeter))