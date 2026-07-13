# WAP to enter P,T,R & calculate simple interest

# Take input for principle,time,rate
p=int(input('Enter a principle:'))
t=int(input('Enter a time:'))
r=int(input('Enter a rate:'))

# calculate simple interest
SI =(p*t*r)/100

# show result
print('A simple interest is',SI)