# Q8. Python program to remove characters of odd index values in a string.

str = input('Enter a string:')
new = ' '
for i in range(0,len(str)):
    if i %2 == 0:
        new = new +str[i]
print('Original string:',str)
print('New string:',new)