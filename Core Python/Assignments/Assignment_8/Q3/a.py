# 3. WAP to find sum of following series using functions.
# a. 1+2+3+4+...+n

def sos(n):
    if n > 0 :
        return n +sos(n-1)
    else:
        return 0
n=int(input('Enter a number:'))
res=sos(n)
print(res)