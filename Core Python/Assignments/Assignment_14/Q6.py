# Q6.Write a program to find the two numbers whose product is maximum among all the pairs in a given list of numbers,
#  use the python set.

li =[5,3,9,6,2]
pairs = set()
for i in range(len(li)):
    for j in range(i+1,len(li)):
        product = li[i] * li[j]
        pairs.add((product,li[i],li[j]))
maximum =0
for pair in pairs:
    if pair[0] > maximum:
        maximum = pair[0]
        num1 =pair[1]
        num2 = pair[2]
print('List:',li)
print('Maximum product:',maximum)
print('Numbers:',num1, 'and',num2)