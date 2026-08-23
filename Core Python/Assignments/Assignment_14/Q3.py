# Q3.WAP to find the all unique words and count the frequency of occurence from a given list of strings use python set data type.

li = ['python','java','c','java','java','python']
s = set(li)
print('List:',li)
print('Unique list:',s)
for words in s:
    count = li.count(words)
    print(words,':',count)