#Q5.Python Program to Sort a List According to the Length of the Elements within the list.

li = ["apple", "cat", "banana", "Hi","dog", "kiwi"]

print("Original list:", li)

li.sort(key=len)

print("Sorted list:", li)