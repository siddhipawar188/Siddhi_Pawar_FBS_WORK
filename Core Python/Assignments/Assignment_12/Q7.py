# Q7. Python program to calculate the length of a string without using library function.

str = input('Enter a string:')
count = 0
for i in str:
    count += 1
print('Length os string:',count)