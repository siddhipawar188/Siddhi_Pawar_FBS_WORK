# Q4. Python program to generate a dictionary that contains numbera (between 1 and n)in the form (x,x*x).

n = int(input('Enter n:'))
d ={}
for i in range(1,n+1):
    d[i]=i * i
print('Dictionary:',d)