# WAP to check whether the triangle is equilateral ,isosceles or scalen.

fs = int(input('Enter first side:'))
ss = int(input('Enter second side:'))
ts = int(input('Enter third side:'))

if(fs == ss == ts):
    print('Triangle is equilateral')
elif(fs == ss or ss == ts or fs == ts):
    print('Triangle is isosceles.')
else:
    print('Triangle is scalen.')