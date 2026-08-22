# Q3. Python program to detect if two strings are anagram.

s1 = input('Enter a string:')
s2 = input('Enter a string:')

if len(s1) != len(s2):
    print('Strings are not anagram.')
else:
    count = 0
    for i in s1:
        if i in s2:
            count += 1
    if count == len(s1):
        print('Strings are anagram.')
    else:
        print('Strings are not anagram.')