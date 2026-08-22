# Q6. Python program to take in a string and replace every blank space with hypen.

str = input('Enter a string:')
new =' '
for i in str:
    if i == ' ':
        new = new + '_'
    else:
        new = new + i
print('Original string:',str)
print('New string:',new) 

# res = str.replace(' ','_')
# print(res)