 # 6. WAP to find print the following fibonacci series using functions:1 1 2 3 5 8 n terms.

def fibonacci_series(n):
    a=-1
    b=1
    for i in range(n):
        c = a + b
        print(c) 
        a = b
        b = c

n = int(input('Enter a number:'))
res = fibonacci_series(n)
print(res)
