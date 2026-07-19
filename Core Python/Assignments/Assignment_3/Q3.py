# WAP to input angles of triangle & check whether triangle is valid or not.

fa = int(input('Enter first angle:'))
sa = int(input('Enter second angle:'))
ta = int(input('Enter third angle:'))

if(fa + sa + ta ==180):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')