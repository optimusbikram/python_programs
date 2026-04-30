#program to calculate simple interest and total amount due
#taking input from user
principal= float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
#calculating simple interest
simple_interest = principal * rate * time / 100
#calculating total amount due]
total_amount_due = principal+ simple_interest
#printing the results
print("Simple Interest : ", simple_interest)
print("Total Amount Due :", total_amount_due)
