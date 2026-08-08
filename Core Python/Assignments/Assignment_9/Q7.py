# Q7.WAP to find sum of digits using recursion.

def sumdigit(num):
    if num > 0:
        d = num % 10
        num = num // 10
        return d + sumdigit(num)
    else:
        return 0
num = int(input('Enter a number:'))
res = sumdigit(num)
print(res)