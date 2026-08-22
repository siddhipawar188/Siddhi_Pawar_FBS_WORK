# Q4. Python program to form a new string where the first character & the last character have been exchanged.

str =input('Enter a string:')
new = str[len(str)-1]
for i in range(1,len(str)-1):
    new = new + str[i]
new = new + str[0]
print('Original string:',str)
print('New string:',new)