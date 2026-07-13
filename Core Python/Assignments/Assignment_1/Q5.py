# WAP to enter P,T,R & calculate compound interest

# Take input for p,t,r
p=int(input('Enter a principle:'))
t=int(input('Enter a time:'))
r=int(input('Enter a rate:'))

# Calculate final amount and compound interest
amount = p* (1+r/ 100)**t
print(amount)
CI = amount - p

# show result
print('The compound interest is',CI)