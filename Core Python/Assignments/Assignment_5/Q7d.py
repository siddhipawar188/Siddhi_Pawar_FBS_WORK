#  WAP to solve the following series.
# d. s= a + a2/2 + a3/3 + ...+ a10/10

a = int(input('Enter number:'))
sum = 0
for i in range(1,11):
    sum = sum +(a ** i)/ i
print('The sum of series:',sum) 