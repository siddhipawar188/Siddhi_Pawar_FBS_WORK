# 8. WAP find reverse of a number.

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        rev = rev * 10 + digit
    return rev
n = int(input('Enter a number:'))
res = reverse_number(n)
print(res)