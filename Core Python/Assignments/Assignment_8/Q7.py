# 7. WAP to find sum of digit of a number.

def sod(n):
    sum = 0
    while n > 0:
        d =n % 10
        n = n//10
        sum = sum + d
    return sum
n = int(input('Enter a number:'))
res = sod(n)
print(res)
 