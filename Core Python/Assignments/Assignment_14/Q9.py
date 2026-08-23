# Q9. Write a python program to find all the unique combinations of 3 numbers from a given list of numbers,
# adding up to a target number.

li =[2,4,7,9,3,5,6,8]
target = 18
print('List:',li)
print('Target:',target)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
            if li[i] + li[j] + li[k] == target:
                print(li[i],li[j],li[k])