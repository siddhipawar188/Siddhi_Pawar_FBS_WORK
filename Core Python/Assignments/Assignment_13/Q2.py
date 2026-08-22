# Q2. Python program to cancatenate two dictionaries into one.

d1 = {'a':10, 'b':20}
d2 = {'c':30,'d':40}
d ={}
for key in d1:
    d[key] = d1[key]
for key in d2:
    d[key] = d2[key]
print('Dictionary1:',d1)
print('Dictionary2:',d2)
print('Cancatenate:',d)