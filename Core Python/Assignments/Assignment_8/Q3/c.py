# c.1^1 + 2^2 + 3^3+....+n^n

def sos(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i ** i)
    return sum
n = int(input('Enter a number:'))
res = sos(n)
print(res)