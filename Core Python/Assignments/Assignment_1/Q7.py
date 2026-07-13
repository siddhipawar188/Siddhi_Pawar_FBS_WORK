# program to find the roots of a quadratic equation

# Take inputs
a=int(input('Enter  a number:'))
b=int(input('Enter  a number:'))
c=int(input('Enter  a number:'))

# Calculate discriminamt
d=b**2 - 4*a*c
print(d)

# Calculate roots
root1= (-b + d**0.5) /(2 * a)
root2= (-b - d**0.5) /(2 * a)

# Display result
print(f'The roots of a quadratic equation is {root1} , {root2}.')