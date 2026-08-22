# Q14. Python program to count the occurence of ach word in a string.

str = input('Enter a string:')
word = str.split()
for i in range(len(word)):
    count = 0
    if word[i] not in word[:i]:
        for j in word:
            if word[i] == j:
                count += 1
        print(word[i],'=',count)
        