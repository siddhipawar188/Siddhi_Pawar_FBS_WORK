# Q12. WAP to create three list of numbers,there  aquare and cube.

li =[1,2,3,4,5]
square =[]
cube =[]
for i in range(0,len(li)):
    square = square +[li[i] ** 2]
    cube = cube + [li[i] ** 3]
print('Original list:',li)
print('Square list:',square)
print('Cube list:',cube)