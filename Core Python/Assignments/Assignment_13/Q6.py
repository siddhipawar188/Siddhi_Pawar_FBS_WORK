# Q6. Python program to multiply all the items in a dictionary.

dict ={'a':1,'b':2,'c':3,'d':4}
multi = 1
for i in dict:
    multi = multi * dict[i]
print('Dictionary:',dict)
print('multiply of all items:',multi)