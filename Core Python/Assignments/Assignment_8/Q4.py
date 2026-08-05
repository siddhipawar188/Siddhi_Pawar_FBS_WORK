# 4. sum of all odd numbers between 1 to n.

def odd_number(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum = sum + i
    return sum
n = int(input('Enter a number:'))
res = odd_number(n)
print(res)







































