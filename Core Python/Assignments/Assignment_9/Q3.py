# Q3.WAP  to reverse a given number using recursive functions.

def reverse(num,rev):
    if num > 0:
        d = num % 10
        rev = rev * 10 + d
        return reverse(num // 10,rev)
    else:
        return rev
num = int(input('Enter a number:'))
res = reverse(num , 0)
print(res)