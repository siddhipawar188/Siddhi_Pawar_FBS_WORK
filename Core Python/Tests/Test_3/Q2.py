# Q2.WAP to calculate the sum of following series where n is input by user.
# 1 /1! + 2/2! +3 /3! + 4 /4!+...n/n!

n = int(input('Enter a number:'))
sum = 0
fact =1

for i in range(1,n+1):
    fact *= i
    sum = sum + (i // fact)
print(sum)