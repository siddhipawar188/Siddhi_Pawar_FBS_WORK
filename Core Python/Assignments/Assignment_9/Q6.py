# Q6. WAP to print fibonacci series using recursion.

def fibonacci(num,a,b):
    if num > 0:
        c = a+b
        print(c,end =' ')
        return fibonacci(num-1,b,c)
num = int(input('Enter a number:'))
print('Fibonacci series:')
fibonacci(num,-1,1)
