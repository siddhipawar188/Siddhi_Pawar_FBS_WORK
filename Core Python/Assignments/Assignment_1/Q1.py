# Take input for 5 subject marks
m1 =int(input('Enter a marks:'))
m2 =int(input('Enter a marks:'))
m3 =int(input('Enter a marks:'))
m4 =int(input('Enter a marks:'))
m5 =int(input('Enter a marks:'))

# Calculate obtained_marks
obtained_marks= (m1+m2+m3+m4+m5)

# Calculate percentage
percentage = ((obtained_marks/500)*100)

# show result
print('The percentage of 5 subject is',percentage)