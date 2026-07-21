# WAP to check if given number is armstrong number or not.

no = int(input('Enter number you want to check:'))
count=len(str(no))
temp = no
total = 0
while(no > 0):
    d=no % 10
    total = total + (d ** count)
    no = no // 10

if(temp == total):
    print(f'The {temp} number is armstrong.')
else:
    print(f'The {temp} number is not armstrong.')