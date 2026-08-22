# Q9. Python program to calculate the number of words and number of characters present in a string.

str = input('Enter a string:')
countch = 0
countwo = 1
for i in str:
    if i != ' ':
        countch += 1
    if i == ' ':
        countwo += 1
print('Number of characters:',countch)
print('Number of words:',countwo)

# words = str.split()
# character = len(str.replace(' ',''))
# print('Number of characters:',character)
# print('Number of words:',len(words))
