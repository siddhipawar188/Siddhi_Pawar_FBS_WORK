# Q11. WAP to print all numbers which are divisible by m and n in the list.

li =[4,6,12,18,24,28]

m = int(input('Enter the value of m:'))
n = int(input('Enter the value of n:'))
for i in li:
    if i % m == 0 and i % n ==0:
        print(i)