# Q7. Python program to remove the given key from a dictionary.

dict = {'id':101,'name':'siddhi','city':'satara','age':21}
key = input('Enter a key to remove:')
if key in dict:
    dict.pop(key)
    print('Updated dictionary:',dict)
else:
    print('Key is does not exist.')