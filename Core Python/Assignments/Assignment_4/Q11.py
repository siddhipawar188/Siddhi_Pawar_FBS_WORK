# WAP to check if given number strong number.

n = int(input('Enter number:'))
temp = n
sum = 0
while(n > 0):
    d = n % 10
    fact = 1
    for i in range(1 , d + 1):
        fact *= i
    sum = sum + fact
    n = n // 10
if(sum == temp):
    print(f'{temp} is a strong number.' )
else:
        print(f'{temp} is  not a strong number.' )
