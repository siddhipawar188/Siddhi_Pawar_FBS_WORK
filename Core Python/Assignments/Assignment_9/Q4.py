# Q4. WAP to find sum of n numbers using recursive.

def sum(num):
    if num > 0:
        return num +sum(num-1)
    else:
        return 0
num = int(input('Enter a number:'))
res = sum(num)
print(res)