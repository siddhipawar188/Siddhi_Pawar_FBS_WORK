# WAp to calculate simple interest based on principle ,rate and time 

p = int(input('Enter a principle:'))
r = int(input('Enter a rate:'))
t = int(input('Enter a time:'))

SI = ((p * r * t)/100)
print('Simple interest:',SI)