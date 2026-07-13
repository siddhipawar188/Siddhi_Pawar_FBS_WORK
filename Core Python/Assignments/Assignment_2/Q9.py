# Q9. WAP to swap two numbers without using third variable.

# Take input for x , y
x = int(input('Enter x:'))
y= int(input('Enter y:'))

# Python Technique
x , y = y , x

# Display result
print(f'After swapping x : {x} , y : {y}.')


# Take input for x ,y 
x = int(input('Enter x:'))
y= int(input('Enter y:'))

# swap without using third variable
x = x + y
y = x - y
x = x - y

# Display result
print(f'After swapping x : {x} , y : {y}.')
