# Q3. Python program to check if a given key exists in a dictionary or not.

d ={'id':101,'name':'siddhi','city':'satara'}
key = input('Enter a key to search:')
if key in d:
    print('Key is exists in dictionary.')
else:
    print('key is does not exists in dictionary.')