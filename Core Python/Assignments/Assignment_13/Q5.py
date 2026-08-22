# Q5. Python program to sum all the items in a dictionary.

dict ={'a':10,'b':20,'c':30}
sum = 0
for i in dict:
    sum = sum + dict[i]
print('Dictionary:',dict)
print('Sum of all items:',sum)