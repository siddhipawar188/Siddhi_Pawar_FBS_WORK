# WAP to prin armstrong number within a given range.

start = int(input('Enter a starting number:'))
end = int(input('Enter a ending number: '))
print('Armostrong numbers are:')
for num in range(start , end + 1):
    temp = num
    digit = len(str(num))
    total = 0
    while(num > 0):
        d = num % 10
        # print(d)
        total = total +(d ** digit)
        # print(total)
        num = num // 10
        # print(num)
    if(total == temp):
        print(total)