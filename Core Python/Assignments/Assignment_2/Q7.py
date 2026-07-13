# Q7. Find the sum of three -digit number.

# Take input 
num = int(input('Enter number:'))

# store num into temp
temp = num
print(temp)

d1 = num % 10
num = num //10
d2 = num % 10
num = num // 10
d3 = num % 10
num = num // 10

# Calculate sum
sum = d1 + d2 + d3

# Disply result
print(f'The sum of three digit number is {sum}')