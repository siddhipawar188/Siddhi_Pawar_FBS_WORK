# Q1. WAP to find sum of following series using recursive functions: 1! + 2! + 3! +.....+ n!

def fact(n):
    if n > 0:
        return n * fact(n-1)
    else:
        return 1

def sumfact(n):
    if n > 0:
        return fact(n) + sumfact(n-1)
    else:
        return 0
n = int(input('Enter a number:'))
res = sumfact(n)
print(res)