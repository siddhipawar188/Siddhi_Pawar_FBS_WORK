# Q1. WAP to print first n prime numbers.

num = int(input('Enter a number:'))
count = 0
n = 2
while count < num:
    for i in range(2,n // 2):
        if n % i == 0:
            break
    else:
        print(n)
        count += 1
    n += 1