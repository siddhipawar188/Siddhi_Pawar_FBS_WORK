#Q10.Write a program to print list after removing even numbers.

li = [10, 25, 37, 45, 59, 67]

new = li.copy()

for i in li:
    if i % 2 == 0:
        new.remove(i)

print("Original List =", li)
print("After Removing Even Numbers =", new)