#area and perimeter of a circle
radius = float(input("Enter the radius of the circle: "))
#calculate the area and perimeter of the circle
area = 3.14 * radius ** 2
perimeter = 2*3.14*radius
#display the result
print("="*50)
print("The area of the circle is: %.4f" %area)
print("The perimeter of the circle is: %.2f" %perimeter)