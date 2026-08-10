# WAP to find second largest element in the list.

li = [13, 22, 9, 57, 1, 56, 8]

max = li[0]
second_max = li[0]

for num in range(1, len(li)):
    if li[num] > max:
        second_max = max
        max = li[num]
    elif li[num] > second_max:
        second_max = li[num]

print('Maximum element:', max)
print('Second maximum element:', second_max)