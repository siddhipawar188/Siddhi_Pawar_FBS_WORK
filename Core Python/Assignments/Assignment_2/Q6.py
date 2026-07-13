# Q6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic,hra=15% of basic.

# Take input for basic
basic = int(input('Enter basic:'))

da = basic * 0.1
ta = basic * 0.12
hra = basic * 0.15

# Calculate total salary
total_salary = basic + da + ta + hra

# Display result
print(f'The totsl salary of employee is {total_salary}.')