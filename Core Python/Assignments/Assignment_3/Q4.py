# WAP to input all sides of a triangle & check whether triangle is valid or not.

fs = int(input('Enter first side:'))
ss = int(input('Enter second side:'))
ts = int(input('Enter third side:'))

if(fs + ss >ts and ss + ts >fs and fs + ts >ss):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')