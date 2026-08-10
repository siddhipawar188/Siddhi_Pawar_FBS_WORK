# Q6. WAP to remove duplicates from the list.

li = [10,20,10,30,40,20,30]
new =[]
for i in li:
    if i not in new:
        new += [i]
print('Original list:',li)
print('New list:',new)