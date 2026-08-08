def power(m,n):
    if n==0:
        return 1
    return m*power(m,n-1)
m=int(input('Enter a m number:'))
n=int(input('Enter a n number:'))
result = power(m,n)
print(f'{m} Raised to the power {n}={result}')