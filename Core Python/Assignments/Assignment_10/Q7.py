# Q7. WAP to create a new list from existing list which contains cube of each number of list.

li = [2,3,4,5]
new=[]
for i in li:
    new += [i ** 3]
print('Original list:',li)
print('New list:',new)