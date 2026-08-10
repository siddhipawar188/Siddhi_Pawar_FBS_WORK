# Q13. WAP to prist list after removing even number.

li = [6, 23, 90, 12, 25, 60]
new = []

for i in li:
    if i % 2 != 0:
        new += [i]

print('Original list:', li)
print('After removing even number:', new)