# Q11. Python program to replace every black space with hypen in a string.

str = input('Enter a string:')
new =' '
for i in str:
    if i == ' ':
        new = new + '-'
    else:
        new = new + i
print('New string:',new) 