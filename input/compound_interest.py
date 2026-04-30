#program to calculate coumpound interest and total amount due
#taking input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
#calculating compound interest
compound_interest = principal * (1+rate/100)**time -principal
#calculating total amount due
total_amount_due = principal + compound_interest
#printing the results
print("Compound Interest : ", compound_interest)
print("total amount due : ", total_amount_due)
