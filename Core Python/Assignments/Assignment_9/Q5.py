# Q5. WAP to find factorial using recursion.

def fact(num):
    if num > 0:
        return num * fact(num-1)
    else:
        return 1
num = int(input('Enter a number:'))
res = fact(num)
print(res)