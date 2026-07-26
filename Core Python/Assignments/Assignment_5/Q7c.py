#  WAP to solve the following series.
# c.Find the sum of geometric series from 1 to n where the common ratio is 2.

n = int(input('Enter number:'))
sum = 0
term = 1
for i in range(1,n+1):
    sum += term
    term *= 2
print('Sum of the geometric series is',sum)  