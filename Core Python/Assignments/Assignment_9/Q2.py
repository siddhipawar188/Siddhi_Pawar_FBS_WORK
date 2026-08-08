# Q2. WAP to check if given number is armstrong or not using recursive function.

def armstrong(num):
    if num > 0:
        digit = num % 10
        return digit ** count + armstrong(num // 10)
    else:
        return 0
num = int(input('Enter a number:'))
count = len(str(num))
res = armstrong(num)
if(res == num):
    print(f'{num} is a armstrong number.')
else:
    print(f'{num} is not a armstrong number.')