# Q13. Python program to count number of digits and letters in a string.

str = input('Enter a string:')
countd= 0
countle = 0
for i in str:
    if i.isdigit():
        countd += 1
    elif(i.isalpha()):
        countle += 1
print('Number of digits:',countd) 
print('Number of letters:',countle)