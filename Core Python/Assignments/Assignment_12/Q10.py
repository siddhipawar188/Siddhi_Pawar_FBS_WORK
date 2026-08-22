# Q10. Python program to take in two strings and display the larger string without using build-in functions.

str1 = input('Enter string:')
str2 = input('Enter string:')
l1 = 0
l2 = 0
for i in str1:
    l1 += 1
for i in str2:
    l2 += 1
if l1 > l2:
    print('Larger string:',str1)
elif(l2 > l1):
    print('Larger string:',str2)
else:
    print('Both strings are equal.')

