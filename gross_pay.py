# gross_pay.py


# Getting user input for hours worked and hourly rate
hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

# Calculate gross pay
gross_pay = hours_worked * hourly_rate

# Output the gross pay
print("Gross pay: $" + str(gross_pay))
