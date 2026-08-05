# 11. WAP to check if a given number is armostrong number or not .for each task create separate function.

def armstrong_number(num):
    temp = num
    sum = 0
    count = len(str(num))

    while(num > 0):
        digit = num % 10
        sum = sum + (digit ** count)
        num = num // 10

    if sum == temp:
        return True
    else:
        return False

num = int(input('Enter a number:'))
res = armstrong_number(num)
print(res)

# if armstrong_number(num):
#     print('Armstrong number.')
# else:
#     print('Not armstrong number.')
