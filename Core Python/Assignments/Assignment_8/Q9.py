# 9. WAP to check ifentered numbers is a palindrome or not.

def palindrome_number(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        num = num // 10 
        rev = rev * 10 + digit
    if rev == temp:
        return True
    else:
        return False
n = int(input('Enter a number:'))
res = palindrome_number(n)
print(res)