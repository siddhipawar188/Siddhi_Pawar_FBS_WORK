# Q10. WAP to remove all occurence of a given element in the list.

li = [10, 20, 30, 20, 40, 20]
new = []

num = int(input('Enter an element: '))

for i in li:
    if i != num:
        new += [i]

print('Original list:', li)
print('New list:', new)