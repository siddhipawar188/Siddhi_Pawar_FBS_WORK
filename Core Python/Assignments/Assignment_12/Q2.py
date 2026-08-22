# Q2. Python program to remove the nth index character froma non empty string.

str = input('Enter a string:')
n = int(input('Enter a index to remove:'))
new = ' '

for i in range(len(str)):
    if i != n:
        new = new + str[i]
print('New string:',new)