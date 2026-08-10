# Q2. WAP to find maximum & minimum element.

li = [13,22,9,57,1,56,8]
max = li[0]
min = li[0]
for num in li :
    if num >max:
        max = num
    if num < min:
        min = num
print(f'max: {max}')
print(f'min: {min}')