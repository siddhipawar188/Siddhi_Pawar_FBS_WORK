# Q8. Python program to count the frequency of words appearing in a string using a dictionary.

s = input('Enter a string:')
words = s.split()
d = {}
for words in words:
    if words in d:
        d[words] =d[words] +1
    else:
        d[words] = 1
print('Word Frequency:',d)