# Q8. WAP to check wheather a number is prime or not.

def prime(num,i):
    if i == num:
        return True
    if num %i==0:
        return False
    return prime(num,i+1)
num = int(input('Enter a number: '))
if num > 1:
    res = prime(num,2)
    if res:
        print('Number is prime.')
    else:
        print('num is not prime.')