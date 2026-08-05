# b. 1! + 2! + 3! + 4! +...+n!

def sof(n):
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact *= i
        sum =sum + fact
    return sum
n = int(input('Enter a number:'))
res =sof(n)
print(res)