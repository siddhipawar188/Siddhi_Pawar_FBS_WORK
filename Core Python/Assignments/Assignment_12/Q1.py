# Q1. python program to replace all occurrences of 'a' with $ in a string.

str = input('Enter a string:')
new =' '

for i in str:
    if i == 'a':
        new += '$'
    else:
        new += i
print('Original string:',str)
print('New string:',new)