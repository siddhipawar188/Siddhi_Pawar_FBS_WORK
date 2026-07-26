#  WAP to solve the following series.
# b. N + N ^2 + N ^3 +N ^4....+N ^ N(Here ^ means exponent).

n = int(input('Enter number:'))
sum = 0
for i in range(1, n+1):
    sum = sum + (n ** i)
print('sum of the series is',sum)