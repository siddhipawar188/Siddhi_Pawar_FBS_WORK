# Q11. WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# Take input for amount
amount = int(input('Enter amount:'))

# Perform calculation
n2000= amount // 2000
amount = amount % 2000

n500 = amount // 500 
amout = amount % 500

n200= amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print(f'2000 notes: {n2000}')
print(f'500 notes: {n500}')
print(f'200 notes: {n200}')
print(f'100 notes: {n100}')
print(f'50 notes: {n50}')
print(f'20 notes: {n20}')
print(f'10 notes: {n10}')

