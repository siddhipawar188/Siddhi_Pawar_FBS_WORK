# Q12. Python program to count number of lowercase characters in a string.

str = input('Enter a string:')
count = 0
for i in str:
    if i.islower():
        count += 1
print('Number of lowercase characters:',count)