# Q10. WAP to reverse three digit number.

# Take input for num
num = int(input('Enter num:'))

# Perform calculation
d1 = num % 10
num = num // 10
d2 = num % 10
num = num // 10
d3 = num % 10
num = num // 10

# Reverse the number
reverse = d1 *100 + d2 * 10 + d3

# Display result
print(f'The reverse number is {reverse}.')