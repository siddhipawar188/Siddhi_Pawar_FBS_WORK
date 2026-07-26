# WAP to solve the following series.
# a. 1! + 2! + 3! + 4! +...+n!

n = int(input('Enter numbers:'))
sum = 0
fact = 1
for i in range(1 , n+1):
    fact *= i
    sum += fact
print('The sum of factorial is',sum)