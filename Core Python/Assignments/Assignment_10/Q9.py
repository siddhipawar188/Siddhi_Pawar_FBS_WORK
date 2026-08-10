# Q9. WAp of having n number of elements in the list & find out even & odd elements in that list & create two separate lists 
# which will have even elements & other will have odd elements.

n = int(input('Enter the number of element:'))
li =[]
for i in range(n):
    num = int(input('Enter a number:'))
    li = li + [num]
even=[]
odd =[]
for i in range(0,len(li)):
    if li[i] % 2 ==0:
        even = even +[li[i]]
    else:
        odd = odd +[li[i]]
print('Original list:',li)
print('Even list:',even)
print('Odd number:',odd)