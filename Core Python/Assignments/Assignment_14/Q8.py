# Q8. Write a python program to find all the programes and group them together from a given list of strings.

strings =['eat','ate','bat','tan','aab','aba','tea','nat']
groups=[]
for word in strings:
    found = False
    for group in groups:
        if len(word) == len(group[0]):
            is_anagram = True
            for ch in set(word):
                if word.count(ch) != group[0].count(ch):
                    is_anagram = False
                    break
            if is_anagram:
                group.append(word)
                found = True
                break
    if not found:
        groups.append([word])
print('List:',strings)
print('Grouped anagrames:')
for group in groups:
    print(group)