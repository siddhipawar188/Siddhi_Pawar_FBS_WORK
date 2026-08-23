# Q5. Write apython program to find the longest common prefix of all strings. use the python set.

str1 = input("Enter strings separated by space: ")
words = str1.split()

prefix = ""

for i in range(len(words[0])):
    s = set()

    for word in words:
        s.add(word[i])

    if len(s) == 1:
        prefix += words[0][i]
    else:
        break

print("Longest Common Prefix =", prefix)