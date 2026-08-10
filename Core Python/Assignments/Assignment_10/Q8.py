# Q8. WAP to create a duplicate of an existing list. it should not point to same list.

li = [10,20,30,40]
new =[]
for i in li:
    new += [i]
print('Original list:',li)
print('Duplicate list:',new)
print(li in new)